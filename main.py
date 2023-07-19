from fastapi import FastAPI

import tools

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]



@app.get("/cpu_times/")
async def cpu_times():
    return tools.get_cpu_times()

@app.get("/cpu_count/")
async def cpu_count():
    return tools.get_cpu_count()

@app.get("/loadavg/")
async def loadavg():
    return tools.get_loadavg()

@app.get("/virtual_memory/")
async def virtual_memory():
    return tools.get_virtual_memory()

@app.get("/swap_memory/")
async def swap_memory():
    return tools.get_swap_memory()

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]    