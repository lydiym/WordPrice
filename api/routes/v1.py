from fastapi import APIRouter


app_v1 = APIRouter()

@app_v1.post('/user')
async def post_user():
    pass

@app_v1.get('/user/{id}')
async def get_user():
    pass

@app_v1.patch('/user/{id}')
async def patch_user():
    pass

@app_v1.post('/message')
async def post_message():
    pass

@app_v1.patch('/message/{id}')
async def get_message():
    pass

@app_v1.get('/messages')
async def get_messages():
    pass

@app_v1.post('/message/{id}/like')
async def post_like():
    pass

@app_v1.get('/message/{id}/like')
async def get_like():
    pass

@app_v1.patch('/message/{id}/like')
async def patch_like():
    pass