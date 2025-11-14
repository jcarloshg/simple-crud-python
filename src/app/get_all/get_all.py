from fastapi import APIRouter
from pydantic import BaseModel, UUID4, Field, ValidationError

# domain
from src.app.shared.domain.custom_response import CustomResponse
from src.app.shared.infra.persist.in_memory.item import items


class ItemsRead(BaseModel):
    uuid: UUID4
    message: str = Field(..., min_length=10, max_length=255)


get_all_items_router = APIRouter()


@get_all_items_router.get("/items")
async def get_all():
    try:

        items_found = []
        for item in items:
            try:
                items_found.append(ItemsRead(**item.dict()))
            except ValidationError as e:
                # Optionally log or handle individual item errors
                continue

        return CustomResponse.success(
            data=items_found,
            msg="Items retrieved successfully",
        )
    except ValidationError as e:
        error_messages = [err['msg'] for err in e.errors()]
        message = "Something went wrong"
        if len(error_messages) > 0:
            message = error_messages[0].split(',')[0]
        return CustomResponse.success(msg=message)
