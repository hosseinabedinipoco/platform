from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/collect")
async def collect_data(request: Request):
    body = await request.body()
    print("📥 New request received!")
    print(f"🔸 Method: {request.method}")
    print(f"🔸 Headers: {dict(request.headers)}")
    print(f"🔸 Body: {body.decode('utf-8')}")
    print("-" * 40)
    return {"status": "received"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
