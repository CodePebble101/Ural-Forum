import logging
import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.scripts.Q_and_A import get_question_data, get_answers_data, get_answer_data

templates = Jinja2Templates(directory="templates")

qa_router = APIRouter(
    prefix="/qa",
    tags=["Вопросы и ответы"],
)



@qa_router.get(path="/question/{parent_answer_id}",
               summary="Получить новый вопрос")
async def get_question(parent_answer_id: int, request: Request):
    try:
        question_data = await get_question_data(request=request, parent_answer_id=parent_answer_id)
        if question_data:
            logging.error(question_data)
            question_data = question_data[0]
            response = {"id": question_data["id"], "text": question_data["text"], "answers": []}
            logging.error(question_data["id"])
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


@qa_router.get(path="/answer/check",
               summary="Проверить правильность ответа")
async def get_question(answer_id: int, request: Request):
    try:

        answer_data = await get_answer_data(request=request, answer_id=answer_id)
        answer_data = answer_data[0]
        response = {"id": answer_data["id"],
                    "message": answer_data["message"],
                    "next_video_id": answer_data["video_id"],
                    "correct": answer_data["correct"]
                    }
        return JSONResponse(status_code=200, content={
            "status": "Success",
            "data": response,
            "details": None
        })

    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail={
            "status": "Error",
            "data": None,
            "details": None
        })
