from pydantic import BaseModel


# основная модель
class ContractsBase(BaseModel):
    project: str
    dogovor_npo: str
    kontract_mzkt: str


# модель ответа со всеми полями
class Contracts(ContractsBase):
    id: int

    class Config:
        orm_mode = True


# модель создания записи
class ContractsCreate(ContractsBase):
    pass


# модель удаления записи
class ContractUpdate(ContractsBase):
    pass
