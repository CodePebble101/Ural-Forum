import os
import sys
import uvicorn
import asyncio

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from app.config.config import DefaultServerSettings, MONGO_URL
from app.endpoints import all_routes

root_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_folder)


def bind_routes(application: FastAPI, settings: DefaultServerSettings, list_of_routes) -> None:
    """
    Bind all routes to application.
    """
    for route in list_of_routes:
        application.include_router(route, prefix=settings.PATH_PREFIX)


def get_app(settings: DefaultServerSettings) -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = "RESTful API for TimeOFF"

    application = FastAPI(
        title="Ural API",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="1.0.0",
    )
    bind_routes(application, settings, all_routes)
    return application


app = get_app(DefaultServerSettings())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE", "PATCH", "PUT"],
    allow_credentials=True,
    allow_headers=["*"]
)
client = AsyncIOMotorClient(MONGO_URL)
app.state.mongo_client = client

templates = Jinja2Templates(directory="app/templates")
@app.get("/")
async def show_video(request: Request):
    video_endpoint = "/ural/api/v1/tests/video/1"
    media_type = "video/mp4"

    return templates.TemplateResponse("video_template.html", {"request": request, "video_endpoint": video_endpoint, "media_type": media_type})



if __name__ == "__main__":
    uvicorn.run(
        app,
        host=DefaultServerSettings().APP_HOST,
        port=DefaultServerSettings().APP_PORT,
        log_level="debug",
    )
