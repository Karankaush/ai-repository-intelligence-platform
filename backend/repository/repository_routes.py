from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user
from repository.repository_service import create_repository, get_user_repositories
from repository.schemas import (CreateRepositoryRequest,RepositoryResponse,)

router = APIRouter(prefix="/repositories",tags=["Repositories"],)


@router.post("",response_model=RepositoryResponse,)
async def create_repository_route(
    data: CreateRepositoryRequest,
    current_user=Depends(get_current_user),
):
    return await create_repository(
        str(current_user["_id"]),
        data,
    )


@router.get(
    "",
    response_model=list[RepositoryResponse]
)
async def get_repositories(
    current_user=Depends(get_current_user)
):

    return await get_user_repositories(
        str(current_user["_id"])
    )