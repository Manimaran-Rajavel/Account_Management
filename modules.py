from sqlalchemy import Column, String, Integer,Float
from database import Base, engine, sessionlocal
from werkzeug.security import generate_password_hash

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(String(355))

class Accounts(Base):
    __tablename__ = "accounts_detail"
    id = Column(Integer, primary_key=True, index=True)
    particulars = Column(String(255))
    credit = Column(Float(255))
    debit = Column(Float(255))
    balance = Column(String(255))

# Create tables (if they don't exist)
Base.metadata.create_all(engine)

# Check if default user exists
session = sessionlocal()

default_user = session.query(User).filter_by(username='Admin').first()

if not default_user:
    hash_password = generate_password_hash('Admin@123')
    default_user = User(username='Admin', password=hash_password)
    session.add(default_user)
    session.commit()
    session.close()