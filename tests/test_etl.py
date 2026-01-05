from pipeline.etl import run_etl
import os

def test_etl_creates_output():
    os.makedirs("pipeline/data", exist_ok=True)
    input_csv = "pipeline/data/input.csv"
    with open(input_csv, "w") as f:
        f.write("id,value\n1,100\n2,200\n3,300\n")
    
    output_file = run_etl()
    assert os.path.exists(output_file)
