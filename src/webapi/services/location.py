from fastapi import Depends
from sqlalchemy.orm import Session
from webapi.database import get_session


class LocationService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session


    # def get_all(self) ->: