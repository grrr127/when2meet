from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.service.meeting_service_mysql import service_create_meeting_mysql

mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"], redirect_slashes=False)


@mysql_router.post(
    "",
    description="meeting 을 생성합니다.",
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_mysql()).url_code)
