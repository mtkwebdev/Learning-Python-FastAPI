from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_api():
    """Root route, sending an example nested dictionary body of data"""
    data = {"data": {"message": "Hello world"}}
    return data
