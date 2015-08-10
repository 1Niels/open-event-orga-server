"""Copyright 2015 Rafal Kowalski"""
from . import db
from .track import Track
from open_event.helpers.date_formatter import DateFormatter


speakers_sessions = db.Table('speakers_sessions',
                    db.Column('speaker_id',
                              db.Integer,
                              db.ForeignKey('speaker.id')),
                    db.Column('session_id',
                              db.Integer,
                              db.ForeignKey('session.id')))

microlocations_sessions = db.Table('microlocations_sessions',
                    db.Column('microlocations_id',
                              db.Integer,
                              db.ForeignKey('microlocations.id')),
                    db.Column('session_id',
                              db.Integer,
                              db.ForeignKey('session.id')))


class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String)
    abstract = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    start_time = db.Column(db.DateTime,
                           nullable=False)
    end_time = db.Column(db.DateTime,
                         nullable=False)
    type = db.Column(db.String)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))
    speakers = db.relationship('Speaker',
                               secondary=speakers_sessions,
                               backref=db.backref('sessions',
                                                  lazy='dynamic'))
    microlocations = db.relationship('Microlocation',
                               secondary=microlocations_sessions,
                               backref=db.backref('sessions',
                                                  lazy='dynamic'))

    level = db.Column(db.String)
    event_id = db.Column(db.Integer,
                         db.ForeignKey('events.id'))

    def __init__(self,
                 title=None,
                 subtitle=None,
                 abstract=None,
                 description=None,
                 start_time=None,
                 end_time=None,
                 type=None,
                 track=None,
                 level=None,
                 microlocation=None,
                 event_id=None):
        self.title = title
        self.subtitle = subtitle
        self.abstract = abstract
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.type = type
        self.track = track
        self.level = level
        self.microlocation = microlocation
        self.event_id = event_id

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'id': self.id,
                'title': self.title,
                'subtitle': self.subtitle,
                'abstract': self.abstract,
                'description': self.description,
                'start_time': DateFormatter().format_date(self.start_time),
                'end_time': DateFormatter().format_date(self.end_time),
                'type': self.type,
                'track': self.track.id if self.track else None,
                'speakers': [speaker.id for speaker in self.speakers],
                'level': self.level,
                'microlocation': self.microlocation.id if self.microlocation else None}

    def __repr__(self):
        return '<Session %r>' % (self.title)


