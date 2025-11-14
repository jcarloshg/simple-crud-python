from fastapi import APIRouter, Request
from pydantic import BaseModel, UUID4, Field, ValidationError

# domain
from src.app.shared.domain.custom_response import CustomResponse
from src.app.shared.infra.persist.in_memory.item import items


class ItemsDto(BaseModel):
    uuid: UUID4
    message: str = Field(..., min_length=10, max_length=255)


create_item_router = APIRouter()


@create_item_router.post("/items")
async def create_item(request: Request):
    try:
        # valid request body
        body = await request.json()
        item = ItemsDto(**body)
        # append to in-memory list
        items.append(item)

        # make response
        # return item
        return CustomResponse.success(
            data=item,
            msg="Item created successfully",
        )
    except ValidationError as e:
        error_messages = [err['msg'] for err in e.errors()]
        message = "Something went wrong"
        if len(error_messages) > 0:
            message = error_messages[0].split(',')[0]
        return CustomResponse.success(msg=message)
