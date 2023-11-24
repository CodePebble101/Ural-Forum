import logging
import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.scripts.question_and_answers import get_question_data, get_answers_data

templates = Jinja2Templates(directory="templates")

qa_router = APIRouter(
    prefix="/qa",
    tags=["Streaming"],
)


@qa_router.get(path='/video/{video_id}',
               summary='Стриминг видео')
async def video_endpoint(video_id: int):
    video_path = f'static/test_video{video_id}.mp4'
    return FileResponse(path=video_path, media_type="video/mp4", )


@qa_router.get(path="/question/{last_quest_id}",
               summary="Получить вопрос")
async def get_question(last_quest_id: int, request: Request):
    try:
        question_data = await get_question_data(request=request, parent_question_id=last_quest_id)
        if question_data:
            question_data = question_data[0]
            response = {"id": question_data["id"], "text": question_data["text"], "answers": []}
            answers_data = await get_answers_data(request=request, question_id=question_data["id"])
            for answer in answers_data:
                response["answers"].append(
                    {
                        "id": answer["id"],
                        "text": answer["text"]
                    }
                )
            return JSONResponse(status_code=200, content={
                "status": "Success",
                "data": response,
                "details": None
            })
        else:
            return JSONResponse(status_code=418, content={
                "status": "Success",
                "data": None,
                "details": "Вопрос не найден"
            }, )
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail={
            "status": "Error",
            "data": None,
            "details": None
        })
