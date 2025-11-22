from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    goal_type = db.Column(db.String(20), nullable=False) # 'time_based' or 'contribution_based'
    target_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, default=0.0)
    target_date = db.Column(db.Date, nullable=True)
    monthly_contribution = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Goal {self.name}>'
