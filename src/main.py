from pathlib import Path

from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

import auth.routes as auth_router
import email_service.routes as email_router
import comment.routes as comment_router
import photo.routes  as photo_router
import userprofile.routes as user_router
import frontend.routes as frontend_router
import tags.routes as tags_router

import middlewares.crutches as crutches

app = FastAPI()

static_path = Path(__file__).parent / 'frontend' / 'static'
app.mount("/static", StaticFiles(directory=static_path), name='static')

app.include_router(auth_router.router)
app.include_router(email_router.router)
app.include_router(comment_router.router)
app.include_router(photo_router.router)
app.include_router(user_router.router)
app.include_router(frontend_router.router)
app.include_router(tags_router.router)


@app.middleware('http')
async def call_header_cookie_crutch(request, call_next):
    return await crutches.cookie_to_header_jwt(request, call_next)


@app.middleware('http')
async def call_response_modificator(request, call_next):
    return await crutches.modify_json_response(request, call_next)


if __name__ == "__main__":
    uvicorn.run(app=app,
                host="localhost",
                port=8080)
