from pydantic import BaseModel


class LocationBase(BaseModel):
    pass


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True


class LocationCreate(LocationBase):
    pass


class LocationUpdate(LocationBase):
    pass
