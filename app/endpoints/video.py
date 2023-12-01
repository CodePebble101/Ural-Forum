import logging

from fastapi import APIRouter, HTTPException
from pathlib import Path
from fastapi import Header
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.templating import Jinja2Templates


video_router = APIRouter(
    prefix="/streaming",
    tags=["Streaming"],
)


@video_router.get(path='/video/{video_id}',
               summary='Стриминг видео', response_class=FileResponse)
async def video_endpoint(video_id: int):
    try:
        video_path = Path(f'app/static/test_video{video_id}.mp4')

        return FileResponse(path=video_path, media_type="video/mp4")
    except FileNotFoundError:
        raise HTTPException(status_code=418, detail={
            "status": "Error",
            "data": None,
            "details": "Видео не найдено"
        })
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail={
            "status": "Error",
            "data": None,
            "details": None
        })