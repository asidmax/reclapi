from fastapi import FastAPI
from api import router


def app():
    application = FastAPI()
    application.include_router(router)
    return application



