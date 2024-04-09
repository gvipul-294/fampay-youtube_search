from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Define the Video model
class Video(Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    published_at = Column(DateTime)
    thumbnail_url = Column(String)

    # Add indexes on title and description
    __table_args__ = (
        Index('idx_title', title),
        Index('idx_description', description),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'published_at': self.published_at.isoformat(),
            'thumbnail_url': self.thumbnail_url
        }