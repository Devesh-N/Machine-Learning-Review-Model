from fastapi import FastAPI
from main import predict_sentiment

app = FastAPI()

@app.get('/{name}')
async def mltrigger(name: str):
    result = predict_sentiment(name)
    return {"Hello": result}
