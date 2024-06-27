from fastapi import FastAPI
from graph import node1
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/nodes")
async def read_nodes_and_edges():
    nodes, edges = node1.to_nodes_and_edges()
    return {"nodes": nodes, "edges": edges}
