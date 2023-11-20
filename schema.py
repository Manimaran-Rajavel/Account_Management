from flask import redirect, render_template, url_for, session, make_response
from modules import User, Accounts
from database import sessionlocal
from sqlalchemy import desc
from werkzeug.security import check_password_hash
import random

class Account_Management:
    def login(username, password):
        
        Session = sessionlocal()
        user = Session.query(User).filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('account_summary'))
        else:
            return render_template('login.html', message = 'Invalid Username or Password')
        
    def record():
        if 'user_id' in session:
            return render_template('add_record.html')
        else:
            return redirect(url_for('index'))
        
    def add_record(particulars, credit, debit, balance):
        if 'user_id' in session:
            Session = sessionlocal()    
            new_user = Accounts(particulars=particulars, credit=credit, debit=debit, balance=balance)
            
            Session.add(new_user)
            Session.commit()
            Session.close()
            particulars=credit=debit=balance=''

            return redirect(url_for('record'))
        else:
            return redirect(url_for('index'))
    
    def display_records():
        if 'user_id' in session:
            Session = sessionlocal()
            data = Session.query(Accounts).order_by(desc(Accounts.id)).all()
            Session.close()

            return render_template('acc_summary.html', data = data)
        else:
            return redirect(url_for('index'))

    def delete_record(id):
        Session = sessionlocal()

        user_to_delete = Session.query(Accounts).filter_by(id=id).first()

        if user_to_delete:
            Session.delete(user_to_delete)
            Session.commit()
            Session.close()
            return redirect(url_for('account_summary'))

    def edit_record(id):
        session['id'] = id
        Session = sessionlocal()

        edit_data = Session.query(Accounts).filter_by(id=id).first()

        return render_template('add_record.html', edit_data=edit_data)
    
    def update(particulars, credit, debit, balance):
        id = session.get('id')
        Session = sessionlocal()
        update = Session.query(Accounts).filter_by(id=id).first()

        if update:
            update.particulars = particulars
            update.credit = credit
            update.debit = debit
            update.balance = balance
            Session.commit()
            Session.close()
            session.clear()
            
        return redirect(url_for('account_summary'))
    
    def logout():
        
        session.pop()
        response = make_response(redirect(url_for('index', _rnd=random.random())))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
