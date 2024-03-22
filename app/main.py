import uvicorn
from fastapi import FastAPI
from tasks import add

app = FastAPI()


@app.get("/inference")
async def inference(a: int, b: int) -> dict:
    result = await add.delay(a, b)  # Redis로 전송
    answer = result.get(timeout=30)  # 10초 동안 작업의 완료를 기다림
    return {"answer": answer}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")
