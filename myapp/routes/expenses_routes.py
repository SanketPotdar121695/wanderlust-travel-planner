from myapp import app
from myapp.controllers.expenses_controllers import get_expenses, create_expense, update_expense, delete_expense

# Expenses Routes
@app.route('/expenses', methods=['GET'])
def expenses_get():
    return get_expenses()

# Create Expense
@app.route('/expenses', methods=['POST'])
def expense_create():
    return create_expense()

# Update Expense
@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def expense_update(expense_id):
    return update_expense(expense_id)

# Delete Expense
@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def expense_delete(expense_id):
    return delete_expense(expense_id)