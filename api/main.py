from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from prediction_service import get_prediction

app = FastAPI()

origins = [
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# declare the http method to use the path
@app.get('/')
async def root():
    return {"message": "Hello World, this is fast API"}

@app.get('/api/market/{market_id}/prediction/{prediction_id}')
def read_prediction(market_id, prediction_id):
    print("is it starting?")
    prediction, prev_close = get_prediction(market_id, prediction_id)

    # advice is always buy low sell high
    if (float(prediction) > float(prev_close)):
        advice = "Price will increasing from last close, you may want to consider selling"
    else:
        advice = "Price dropping from last close, you may want to hold"

    
    json_data = {
        "prediction": str(prediction),
        "previous_close": str(prev_close),
        "market" : str(market_id),
        "prediction_id": str(prediction_id),
        "advice" : str(advice)
    }
    
    return json_data

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8080)