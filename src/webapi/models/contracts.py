from pydantic import BaseModel


class ContractsBase(BaseModel):
    project: str
    dogovor_npo: str
    kontract_mzkt: str


class Contracts(ContractsBase):
    id: int

    class Config:
        orm_mode = True

class ContractsCreate(ContractsBase):
    pass

class ContractUpdate(ContractsBase):
    pass