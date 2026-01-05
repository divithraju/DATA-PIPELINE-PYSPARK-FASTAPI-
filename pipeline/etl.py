import os
from pyspark.sql import DataFrame
from .spark_config import get_spark_session

DATA_INPUT = os.getenv("DATA_INPUT", "pipeline/data/input.csv")
DATA_OUTPUT = os.getenv("DATA_OUTPUT", "pipeline/data/output.parquet")

def run_etl(input_path=DATA_INPUT, output_path=DATA_OUTPUT) -> str:
    spark = get_spark_session()
    
    # Read CSV
    df = spark.read.option("header", True).csv(input_path)
    
    # Simple transformation: drop nulls, cast numeric columns
    for col in df.columns:
        df = df.na.drop(subset=[col])
    
    df.write.mode("overwrite").parquet(output_path)
    spark.stop()
    return output_path

if __name__ == "__main__":
    os.makedirs("pipeline/data", exist_ok=True)
    # Sample CSV if not exist
    if not os.path.exists(DATA_INPUT):
        with open(DATA_INPUT, "w") as f:
            f.write("id,value\n1,100\n2,200\n3,300\n")
    output = run_etl()
    print(f"ETL complete. Output saved at: {output}")
