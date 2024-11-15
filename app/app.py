from fastapi import FastAPI

app = FastAPI(
    title="Github Actions - testing APIs"
)

@app.get('/home')
async def home():
    return {
        "message": "Hello! This is Home page!"
    }

@app.get('/ci-cd-stuff')
async def ci_cd_stuff():
    return {
        "status": "success",
        "data": {
            "message": "This is a CI-CD pipeline test",
            "description": "This is a test to check the CI-CD pipeline!!",
            "status": "successful"
        }
    }

@app.get('/added-path')
async def added_path():
    return {
        "/added-path": "Added through CI-CD pipeline"
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