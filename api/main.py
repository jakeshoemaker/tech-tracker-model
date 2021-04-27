from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import uvicorn
from prediction_service import get_prediction

app = FastAPI()

# declare the http method to use the path
@app.get('/')
async def root():
    return {"message": "Hello World, this is fast API"}

@app.get('/api/market/{market_id}/prediction/{prediction_id}')
def read_prediction(market_id, prediction_id):
    print("is it starting?")
    prediction, prev_close = get_prediction(market_id, prediction_id)

    if (float(prediction) > float(prev_close)):
        advice = "Price prediciton increasing from last close, consider holding"
    else:
        advice = "Price dropping from last close, please check stocks"

    
    json_data = {
        "prediction": str(prediction),
        "previous close": str(prev_close),
        "market" : str(market_id),
        "prediction_id": str(prediction_id),
        "advise" : str(advice)
    }
    
    return json_data

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)