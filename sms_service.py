from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Boolean,
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship, declarative_base, backref
from datetime import datetime

Base = declarative_base()

# Association table to link SMS and User, and store message confirmation details
sms_user = Table(
    'sms_user', Base.metadata,
    Column('sms_id', Integer, ForeignKey('sms.id', ondelete="CASCADE"), primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id', ondelete="CASCADE"), primary_key=True),
    Column('delivered', Boolean, default=False),  # Indicates if the message was delivered
    Column('delivery_timestamp', DateTime),       # Time of delivery confirmation
)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    phone_number = Column(String(15), unique=True, nullable=False)  # User's phone number

    # Relationship to SMS through the association table
    messages = relationship(
        "SMS",
        secondary=sms_user,
        back_populates="recipients"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, phone_number={self.phone_number})>"

class SMS(Base):
    __tablename__ = 'sms'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)  # Content of the SMS
    sender_name = Column(String(50), nullable=False)  # Name of the sender (e.g., Info)
    sent_at = Column(DateTime, default=datetime.utcnow)  # Timestamp of when the SMS was sent

    # Relationship to User through the association table
    recipients = relationship(
        "User",
        secondary=sms_user,
        back_populates="messages"
    )

    def __repr__(self):
        return f"<SMS(id={self.id}, content='{self.content}', sender_name={self.sender_name}, sent_at={self.sent_at})>"