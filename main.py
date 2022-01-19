from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import (save_data_to_db, get_data_from_db)

# instantiate fastapi
app = FastAPI()


@app.get('/')
def root():
    save_data_to_db()
    result = get_data_from_db()
    if result:
        return result
    raise HTTPException(300, "Something went wrong")
