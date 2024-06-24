from fastapi import FastAPI, Request
import requests
from bot import bot, API_TOKEN, dp 
from aiogram import types
import uvicorn

app = FastAPI()

@app.on_event("startup") 
async def on_startup(): 
    webhook_url = 'https://25fb-5-130-33-200.ngrok-free.app'
    telegram_api_url = f'https://api.telegram.org/bot{API_TOKEN}/setWebhook'
    response = requests.post(telegram_api_url, data={"url": webhook_url}) 
    print(response.json())

@app.on_event("shutdown")
async def on_shutdown():
     telegram_api_url = f'https://api.telegram.org/bot{API_TOKEN}/deleteWebhook' 
     response = requests.post(telegram_api_url)
     print(response.json())
@app.post("/")
async def webhook(request: Request):
    json_data = await request.json() 
    update = types.Update(**json_data) 
    await dp.feed_update(bot = bot,update = update)
if __name__ == '__main__':
    uvicorn.run(app,host = '0.0.0.0', port = 8000)


