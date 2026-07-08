from datetime import datetime, timezone
from repository.repository_mapper import repository_to_response
from bson import ObjectId
from fastapi import HTTPException

from database.mongodb import db

repositories_collection = db["repositories"]


async def create_repository(user_id: str, data):

    repository = {
        "user_id": ObjectId(user_id),
        "name": data.name,
        "description": data.description,
        "source": data.source,
        "status": "created",
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
    }

    result = await repositories_collection.insert_one(repository)
    repository["_id"] = result.inserted_id

    return repository_to_response(repository)

   




async def get_user_repositories(user_id: str):

    repositories = await repositories_collection.find(
        {
            "user_id": ObjectId(user_id)
        }
    ).to_list(length=None)
    return [
        repository_to_response(repository)
        for repository in repositories
    ]


async def get_repository_by_id(
    repository_id: str,
    user_id: str,
):

    repository = await repositories_collection.find_one(
        {
            "_id": ObjectId(repository_id),
            "user_id": ObjectId(user_id),
        }
    )

    if not repository:
        raise HTTPException(
            status_code=404,
            detail="Repository not found",
        )

    return repository_to_response(repository)






async def delete_repository(
    repository_id: str,
    user_id: str,
):

    result = await repositories_collection.delete_one(
        {
            "_id": ObjectId(repository_id),
            "user_id": ObjectId(user_id),
        }
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Repository not found",
        )

    return {
        "message": "Repository deleted successfully"
    }