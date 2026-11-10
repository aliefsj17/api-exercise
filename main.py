from fastapi import FastAPI, HTTPException
import pandas as pd

#Create Object FastAPI

app = FastAPI()

#endpoint = get data halaman utama
@app.get("/")
def handleGetData():
    # .... ada proses yang berjalan

    return {
        "message": "hello world!"
    }

# endpoint -> get data from csv
@app.get("/data")
def handleCSV():
    # 1. baca data dari CSV
    df = pd.read_csv('mock-employees.csv')

    # 2. Ubah DataFrame ke JSON
    df = df.to_dict(orient="records")

    # 3. Return JSON
    return {
        "data": df
    }

#endpoint -> get data by id (filter)
@app.get("/data/{id}")
def handlefilter(id: int):
    #1. baca data CSV
    df= pd.read_csv("mock-employees.csv")

    #2. Filter Data colomn: id
    df [df["id]"] == id]

    #2.1 Error Handling: ketika hasil filter kosong,
    # -> maka tampilkan pesan error
    if df.empty == True:
        raise HTTPException(status_code=404, detail="data tidak ditemukan!")
    #Gak perlu ada Else karena Raise fungsinya sama dengan Return
    
    #3. Ubah df -> JSON
    df = df.to_dict(orient="records")

    #4, return JSON
    return {"data": df}