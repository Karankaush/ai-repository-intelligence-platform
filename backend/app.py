from fastapi import FastAPI

app = FastAPI(
    title="AI Repository Intelligence Platform",
    version= "0.1.0"
)

@app.get('/')
async def home():
    return {"message": "Welcome to the AI Repository Intelligence Platform!"}



@app.get('/health')
async def health():
    return{
        "status" : 'healthy'
    }