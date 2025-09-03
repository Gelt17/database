from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Genre(Base):
    __tablename__ = "genre"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_genre = Column(String(255), nullable=False, unique=True)
    
    books = relationship("Book", back_populates="genre")

class Author(Base):
    __tablename__ = "author"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_author = Column(String(255), nullable=False)
    
    books = relationship("Book", back_populates="author")

class City(Base):
    __tablename__ = "city"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_city = Column(String(255), nullable=False, unique=True)
    days_delivery = Column(Integer, nullable=False)
    
    clients = relationship("Client", back_populates="city")  # ИСПРАВЛЕНО

class Book(Base):
    __tablename__ = "book"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    genre_id = Column(Integer, ForeignKey("genre.id"), nullable=False)
    price = Column(Integer, nullable=False)
    amount = Column(Integer, default=0)    
    
    genre = relationship("Genre", back_populates="books")  # ИСПРАВЛЕНО
    author = relationship("Author", back_populates="books")  # ИСПРАВЛЕНО
    order_books = relationship("OrderBook", back_populates="book")

class Client(Base):
    __tablename__ = "client"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    
    city = relationship("City", back_populates="clients")
    orders = relationship("Order", back_populates="client")

class Order(Base):
    __tablename__ = "order"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    buy_description = Column(Text, nullable=True)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)

    client = relationship("Client", back_populates="orders")
    order_books = relationship("OrderBook", back_populates="order")
    order_steps = relationship("OrderStep", back_populates="order")  # ДОБАВЛЕНО

class OrderBook(Base):
    __tablename__ = "order_book"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
    amount = Column(Integer, nullable=False, default=1)
    
    order = relationship("Order", back_populates="order_books")
    book = relationship("Book", back_populates="order_books")

class Step(Base):
    __tablename__ = "step"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    
    order_steps = relationship("OrderStep", back_populates="step")

class OrderStep(Base):
    __tablename__ = "order_step"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)  # ИСПРАВЛЕНО
    step_id = Column(Integer, ForeignKey('step.id'), nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    
    order = relationship("Order", back_populates="order_steps")  # Теперь правильно
    step = relationship("Step", back_populates="order_steps")