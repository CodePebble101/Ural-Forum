from app.endpoints.video import video_router
from app.endpoints.questions_and_answers import qa_router

all_routes = [video_router,qa_router]

__all__ = [
    'all_routes'
]
