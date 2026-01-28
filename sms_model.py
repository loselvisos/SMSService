from datetime import datetime

class SMS(Base):
    __tablename__ = 'sms'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    sender_name = Column(String(50), nullable=False)
    sent_at = Column(
      Timestamp)