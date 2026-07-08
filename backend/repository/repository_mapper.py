def repository_to_response(repository):

    return {
        "id": str(repository["_id"]),
        "user_id": str(repository["user_id"]),
        "name": repository["name"],
        "description": repository["description"],
        "source": repository["source"],
        "status": repository["status"],
        "created_at": repository["created_at"],
    }