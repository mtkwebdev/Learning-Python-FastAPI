from fastapi import FastAPI

app = FastAPI()

example_data = {"data": {"message": "Hello world"}}

@app.get("/")
def get_root():
    """Root route, sending an example nested dictionary body of data"""
    return example_data

@app.get("/{name}")
def get_dynamic_path_by_name(name:str):
    """A dynamic route that will return a message based on the route path parameter"""
    copy_of_example_data = example_data
    copy_of_example_data["data"].update({"message": name})
    return copy_of_example_data
