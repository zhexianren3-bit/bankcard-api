from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "银行卡API"}
@app.get("/info")
def info(no: str = ""):
    return {"success": True, "bank": "工商银行", "type": "借记卡"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
