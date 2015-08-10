"""Copyright 2015 Rafal Kowalski"""
from ..models.event import Event
from ..models.session import Session
from ..models.track import Track
from ..models.speaker import Speaker
from ..models.sponsor import Sponsor
from ..models.microlocation import Microlocation
from ..models.user import User
from ..models.file import File
from open_event.helpers.helpers import get_event_id
from flask.ext import login


class DataGetter:
    @staticmethod
    def get_all_events():
        """Method return all events"""
        return Event.query.all()

    @staticmethod
    def get_event(event_id):
        """Method return Event with proper event_id"""
        return Event.query.get(event_id)

    @staticmethod
    def get_all_owner_events(owner_id):
        """Method return all owner events"""
        return Event.query.filter_by(owner=owner_id)

    @staticmethod
    def get_sessions_by_event_id():
        """
        :return: All Sessions with correct event_id
        """
        return Session.query.filter_by(event_id=get_event_id())

    @staticmethod
    def get_tracks(event_id):
        """
        :param event_id: Event id
        :return: All Track with event id
        """
        return Track.query.filter_by(event_id=event_id)

    @staticmethod
    def get_track(track_id):
        """
        :param track_id: Track id
        :return: Track object with proper track_id
        """
        return Track.query.get(track_id)

    @staticmethod
    def get_sessions(event_id):
        """
        :param event_id: Event id
        :return: Return all Sessions objects with Event id
        """
        return Session.query.filter_by(event_id=event_id)

    @staticmethod
    def get_session(session_id):
        """
        :param session_id: Session id
        :return: Session with session_id
        """
        return Session.query.get(session_id)

    @staticmethod
    def get_speakers(event_id):
        """
        :param event_id: Event id
        :return: Speaker objects filter by event_id
        """
        return Speaker.query.filter_by(event_id=event_id)

    @staticmethod
    def get_speakers_by_event_id():
        """
        :param event_id: Event id
        :return: Speaker objects filter by event_id
        """
        return Speaker.query.filter_by(event_id=get_event_id())

    @staticmethod
    def get_speaker(speaker_id):
        """
        :param speaker_id: Speaker id
        :return: Speaker object with speaker_id
        """
        return Speaker.query.get(speaker_id)

    @staticmethod
    def get_sponsors(event_id):
        """
        :param event_id: Event id
        :return: All Sponsors fitered by event_id
        """
        return Sponsor.query.filter_by(event_id=event_id)

    @staticmethod
    def get_sponsor(sponsor_id):
        """
        :param sponsor_id: Sponsor id
        :return: Sponsor with sponsor_id
        """
        return Sponsor.query.get(sponsor_id)

    @staticmethod
    def get_microlocations_by_id():
        """
        :param event_id: Event id
        :return: All Microlocation filtered by event_id
        """
        return Microlocation.query.filter_by(event_id=get_event_id())

    @staticmethod
    def get_microlocations(event_id):
        """
        :param event_id: Event id
        :return: All Microlocation filtered by event_id
        """
        return Microlocation.query.filter_by(event_id=event_id)

    @staticmethod
    def get_microlocation(microlocation_id):
        """
        :param microlocation_id: Microlocation id
        :return: Microlocation with microlocation_id
        """
        return Microlocation.query.get(microlocation_id)

    @staticmethod
    def get_event_owner(event_id):
        """
        :param event_id: Event id
        :return: Owner of proper event
        """
        owner_id = Event.query.get(event_id).owner
        return User.query.get(owner_id).login

    @staticmethod
    def get_all_files_tuple():
        """
        :return All files filtered by owner, Format [(test.png, test1.png)...]:
        """
        files = File.query.filter_by(owner_id=login.current_user.id)
        print files
        return [(file.name, file.name) for file in files]

    @staticmethod
    def get_all_microlocations_tuple():
        """
        :return All files filtered by owner, Format [(test.png, test1.png)...]:
        """
        microlocations = DataGetter.get_microlocations_by_id()
        return [(microlocation.id, microlocation.name) for microlocation in microlocations]

    @staticmethod
    def get_all_owner_files():
        """
        :return: All owner files
        """
        files = File.query.filter_by(owner_id=login.current_user.id)
        return files