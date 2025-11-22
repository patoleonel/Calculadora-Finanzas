import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, Goal
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-please-change-in-prod')

# Database configuration
database_url = os.environ.get('DATABASE_URL', 'sqlite:///goals.db')
# Fix for some hosting providers using postgres:// instead of postgresql://
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    goals = Goal.query.all()
    return render_template('index.html', goals=goals)

@app.route('/add', methods=['GET', 'POST'])
def add_goal():
    if request.method == 'POST':
        name = request.form['name']
        goal_type = request.form['goal_type']
        target_amount = float(request.form['target_amount'])
        current_amount = float(request.form['current_amount'])
        
        target_date = None
        monthly_contribution = None
        
        if goal_type == 'time_based':
            target_date_str = request.form['target_date']
            if target_date_str:
                target_date = datetime.strptime(target_date_str, '%Y-%m-%d').date()
                # Calculate monthly contribution
                today = datetime.now().date()
                months = (target_date.year - today.year) * 12 + (target_date.month - today.month)
                if months > 0:
                    monthly_contribution = (target_amount - current_amount) / months
                else:
                    monthly_contribution = target_amount - current_amount # Due immediately
        
        elif goal_type == 'contribution_based':
            monthly_contribution = float(request.form['monthly_contribution'])
            # Calculate target date
            if monthly_contribution > 0:
                months_needed = (target_amount - current_amount) / monthly_contribution
                # This is a rough estimation, could be improved with exact date math
                import dateutil.relativedelta
                today = datetime.now().date()
                target_date = today + dateutil.relativedelta.relativedelta(months=int(months_needed))

        new_goal = Goal(
            name=name,
            goal_type=goal_type,
            target_amount=target_amount,
            current_amount=current_amount,
            target_date=target_date,
            monthly_contribution=monthly_contribution
        )
        
        db.session.add(new_goal)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add_goal.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
