from sqlalchemy import Table, Column, Integer, ForeignKey, String, Date
from config.db import db
from datetime import datetime, timedelta

cart_items_association = Table(
    'cart_items_association', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('book_id', Integer, ForeignKey('store_books.id'), primary_key=True),
    Column('quantity', Integer, nullable=False)
)

borrowings_association = Table(
    'borrowings_association', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('book_id', Integer, ForeignKey('library_books.id'), primary_key=True),
    Column('date_borrowed', Date, default=datetime.utcnow),
    Column('due_date', Date, default=lambda: datetime.utcnow() + timedelta(days=70)),
    Column('date_returned', Date),
    Column('status', String, default='Pending')
)
