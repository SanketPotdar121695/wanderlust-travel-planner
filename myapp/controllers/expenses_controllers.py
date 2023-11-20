import datetime
from myapp import db
from myapp.models import Expense
from flask import jsonify, request

# Expenses Routes
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([{'id': exp.id, 'description': exp.description, 'amount': exp.amount, 'date': exp.date, 'destination_id': exp.destination_id} for exp in expenses])

# Create Expense
def create_expense():
    data = request.get_json()
    new_expense = Expense(description=data['description'], amount=data['amount'], date=datetime.utcnow(), destination_id=data['destination_id'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense created successfully'})

# Update Expense
def update_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense is None:
        return jsonify({'error': 'Expense not found'}), 404

    data = request.get_json()
    expense.description = data['description']
    expense.amount = data['amount']
    expense.date = datetime.utcnow()

    db.session.commit()
    return jsonify({'message': 'Expense updated successfully'})

# Delete Expense
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense is None:
        return jsonify({'error': 'Expense not found'}), 404

    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': 'Expense deleted successfully'})