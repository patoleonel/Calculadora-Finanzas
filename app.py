import os
import math
from flask import Flask, render_template, request
from datetime import datetime
import dateutil.relativedelta

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-please-change-in-prod')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        try:
            name = request.form.get('name', 'Meta')
            goal_type = request.form['goal_type']
            target_amount = float(request.form['target_amount'])
            current_amount = float(request.form['current_amount'])
            interest_rate = float(request.form.get('interest_rate', 0.0))
            
            # Monthly interest rate
            r = interest_rate / 100 / 12
            
            result = {
                'name': name,
                'goal_type': goal_type,
                'target_amount': target_amount,
                'current_amount': current_amount,
                'interest_rate': interest_rate
            }

            if goal_type == 'time_based':
                target_date_str = request.form['target_date']
                if target_date_str:
                    target_date = datetime.strptime(target_date_str, '%Y-%m-%d').date()
                    result['target_date'] = target_date
                    
                    # Calculate monthly contribution
                    today = datetime.now().date()
                    months = (target_date.year - today.year) * 12 + (target_date.month - today.month)
                    
                    if months > 0:
                        if r > 0:
                            # Compound interest formula for PMT
                            numerator = (target_amount - current_amount * math.pow(1 + r, months)) * r
                            denominator = math.pow(1 + r, months) - 1
                            monthly_contribution = numerator / denominator
                        else:
                            monthly_contribution = (target_amount - current_amount) / months
                    else:
                        monthly_contribution = target_amount - current_amount # Due immediately
                    
                    result['monthly_contribution'] = monthly_contribution
            
            elif goal_type == 'contribution_based':
                monthly_contribution = float(request.form['monthly_contribution'])
                result['monthly_contribution'] = monthly_contribution
                
                # Calculate target date
                if monthly_contribution > 0:
                    months_needed = 0
                    if r > 0:
                        # Compound interest formula for n
                        try:
                            numerator = target_amount * r + monthly_contribution
                            denominator = current_amount * r + monthly_contribution
                            # Check for valid log input
                            if numerator > 0 and denominator > 0:
                                months_needed = math.log(numerator / denominator) / math.log(1 + r)
                            else:
                                months_needed = 0 # Should not happen with positive amounts
                        except ValueError:
                            months_needed = (target_amount - current_amount) / monthly_contribution
                    else:
                        months_needed = (target_amount - current_amount) / monthly_contribution
                    
                    today = datetime.now().date()
                    target_date = today + dateutil.relativedelta.relativedelta(months=int(months_needed))
                    result['target_date'] = target_date

        except Exception as e:
            print(f"Error calculating goal: {e}")
            # In a real app, you might want to flash an error message here
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
