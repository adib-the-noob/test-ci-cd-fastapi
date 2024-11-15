from fastapi import FastAPI

app = FastAPI(
    title="Github Actions - testing APIs"
)

@app.get('/home')
async def home():
    return {
        "message": "Hello! This is Home page!"
    }

@app.get('/')
async def root():
    return {
        "message" : {
            "path" : "/",
            "method" : "GET",
            "message" : "Hello! This is the root page!"
        }
    }