import logging
import os

from fastapi import APIRouter
from fastapi import Header
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates(directory="templates")

video_router = APIRouter(
    prefix="/tests",
    tags=["Streaming"],
)

CHUNK_SIZE = 1024 * 1024


@video_router.get(path='/video/{question_id}',
                  summary='Стриминг видео')
async def video_endpoint(question_id: int):
    video_id = 1
    video_path = f'static/test_video{video_id}.mp4'
    return FileResponse(path=video_path, media_type="video/mp4",)

