from twilio.rest import Client
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Twilio setup
client = Client("ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "your_auth_token")
message_body = '''Hey A Y! 🎉
We’re throwing a party this weekend and would love for you to come by. 
Hope to catch up and share some laughs. Let me know!'''

client.messages.create(to="+11234567890", from_="+10987654321", body=message_body)

# ORM setup
Base = declarative_base()
class MessageLog(Base):
    __tablename__ = 'messages'
    id = Column(String, primary_key=True)
    body = Column(String)
    sent_at = Column(DateTime)

engine = create_engine('sqlite:///messages.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(MessageLog(id="mock_user_123", body=message_body, sent_at=datetime.now()))
session.commit()
