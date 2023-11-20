from flask import Flask, render_template, request
from schema import Account_Management

app = Flask(__name__)
app.secret_key = "1001"


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        result = Account_Management.login(username, password)

    return result

@app.route('/acc_summary/')
def account_summary():
    result = Account_Management.display_records()
    return result

@app.route('/record')
def record():
    return Account_Management.record()

@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    if request.method == 'POST':
        particulars = request.form.get('particulars')
        credit = request.form.get('credit')
        debit = request.form.get('debit')
        balance = request.form.get('balance')
        
        result = Account_Management.add_record(particulars, credit, debit, balance)

    return result

@app.route('/delete/<id>')
def delete_record(id):
    result = Account_Management.delete_record(id)
    return result

@app.route('/edit/<id>')
def edit_record(id):
    result = Account_Management.edit_record(id)
    return result

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        particulars = request.form.get('particulars')
        credit = request.form.get('credit')
        debit = request.form.get('debit')
        balance = request.form.get('balance')
        result = Account_Management.update(particulars, credit, debit, balance)

    return result

@app.route('/logout')
def logout():
    
    return Account_Management.logout()



if __name__ == "__main__":
    app.run(debug=False)
