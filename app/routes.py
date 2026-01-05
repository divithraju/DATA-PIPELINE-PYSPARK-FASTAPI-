from fastapi import APIRouter
from pydantic import BaseModel
from pipeline.etl import run_etl
import pandas as pd
import os

router = APIRouter()

class QueryResponse(BaseModel):
    records: list
    total: int

@router.get("/data", response_model=QueryResponse)
def get_processed_data():
    output_path = os.getenv("DATA_OUTPUT", "pipeline/data/output.parquet")
    
    if not os.path.exists(output_path):
        run_etl()
    
    df = pd.read_parquet(output_path)
    records = df.to_dict(orient="records")
    
    return QueryResponse(records=records, total=len(records))
