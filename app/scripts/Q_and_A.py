import json
import logging

from motor.motor_asyncio import AsyncIOMotorClient


async def get_question_data(request, parent_answer_id: int) ->list:
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client['test_db']
    cursor = mongo_client.questions.find({"parent_answer_id": parent_answer_id})
    result_data = []
    for document in await cursor.to_list(length=100):
        document["_id"] = str(document["_id"])
        result_data.append(document)
    return result_data


async def get_answers_data(request, question_id: int)->list:
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client['test_db']
    cursor = mongo_client.answers.find({"question_id": question_id})
    result_data = []
    for document in await cursor.to_list(length=100):
        document["_id"] = str(document["_id"])
        result_data.append(document)
        logging.error(document)
    return result_data


async def get_answer_data(request, answer_id: int):
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client['test_db']
    cursor = mongo_client.answers.find({"id": answer_id})
    result_data = []
    for document in await cursor.to_list(length=100):
        document["_id"] = str(document["_id"])
        result_data.append(document)
    return result_data