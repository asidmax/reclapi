from typing import List
from fastapi import Depends, HTTPException, status, Response

from webapi import tables
from sqlalchemy.orm import Session
from webapi.database import get_session
from typing import List, Optional
from src.webapi.models.contracts import Contracts, ContractsCreate, ContractUpdate


class ReclService():
    # создание объекта сессии
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, project_id: int) -> tables.Contract:
        project_by_id = self.session.query(tables.Contract).filter_by(id=project_id).first()
        if not project_by_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return project_by_id

    def get_list(self, project: Optional[str] = None) -> List[tables.Contract]:  # возвращает лист из таблицы
        query = self.session.query(tables.Contract)
        if project:
            query = query.filter_by(project=project)
        oper = query.all()
        return oper

    def get_id(self, project_id: int) -> tables.Contract:
        return self._get(project_id)

    def create(self, project_data: ContractsCreate) -> tables.Contract:
        operation = tables.Contract(**project_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, project_id: int, update_data: ContractUpdate):
        contract = self._get(project_id)
        for field, value in update_data:
            setattr(contract, field, value)
        self.session.commit()
        return contract

    def delete(self, project_id: int):
        deleted_project = self._get(project_id)
        self.session.delete(deleted_project)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)