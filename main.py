from fastapi import FastAPI, Path
from fastapi.responses import PlainTextResponse

app = FastAPI(title= 'Govno')



@app.get("/")
def root():
    return {"message": "Hello pidar"}


@app.get("/add")
def add(x: int, y: int) -> int:
    return x + y


@app.get("/double/{number}")
def double(number: int) -> int:
    return number * 2


@app.get("/welcome/{name}&{surname}")
def welcome(name: str = Path(max_length=15, min_length=2),
            surname: str = Path(max_length=15, min_length=3)) -> str:
    return f'Hello {name},{surname} ti pidar'


@app.get("/text")
def get_text():
    content = 'Zalupa kakayato'
    return PlainTextResponse(content=content)



