from fastapi import APIRouter, Depends
from typing import List, Optional
from src.webapi.services.recl import ReclService
from src.webapi.models.contracts import Contracts, ContractsCreate, ContractUpdate

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Contracts])
def index(
        project: Optional[str] = None,
        service: ReclService = Depends()
):
    return service.get_list(project=project)


@router.get('/{project_id', response_model=Contracts)
def get_by_id(
        project_id: int,
        service: ReclService = Depends()
):
    return service.get_id(project_id)


@router.post('/', response_model=Contracts)
def create(
        project_data: ContractsCreate,
        service: ReclService = Depends()
):
    return service.create(project_data)


@router.put('/{project_id}', response_model=Contracts)
def update_project(
        project_id: int,
        project_data: ContractUpdate,
        service: ReclService = Depends()
):
    return service.update(project_id, project_data)

@router.delete('/{project_id}')
def delete(
        project_id: int,
        service: ReclService = Depends()
):
    return service.delete(project_id)