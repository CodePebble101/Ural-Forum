from motor.motor_asyncio import AsyncIOMotorClient


async def get_question_data(request, parent_question_id: int) ->list:
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client['test_db']
    cursor = mongo_client.questions.find({"parent_id": parent_question_id})
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
    return result_data
