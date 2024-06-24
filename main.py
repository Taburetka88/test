from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel
import bot
import asyncio
app = FastAPI()


class Tg_message(BaseModel):
    tg_id: int
    message: str 


@app.post("/")
async def send_massage(message: Tg_message):
    await bot.bot.send_message(message.tg_id, message.message)
    return 200
@app.on_event("startup")
async def on_sturtup():
    asyncio.create_task(bot.start_bot())
