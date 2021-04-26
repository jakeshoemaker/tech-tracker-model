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

@app.get('/market/{market_id}/prediction/{prediction_id}')
def read_prediction(market_id, prediction_id):
    print("is it starting?")
    prediction = get_prediction(market_id, prediction_id)
    json_data = {
        "prediction": str(prediction),
        "market" : str(market_id),
        "prediction_id": str(prediction_id)
    }
    
    return json_data

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)