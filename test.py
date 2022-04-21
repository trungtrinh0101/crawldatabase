import uvicorn
from fastapi import FastAPI
import mysql.connector
from typing import Optional

class Item():
    title: str
    price: str
    description: Optional[str] = None
    distCity:str
    uptime: str
    productArea: str

app = FastAPI()


def fetch_data(connection):

    query = 'SELECT * FROM databds'
    cursor = connection.cursor()
    results = cursor.execute(query).fetchall()
    print(results)

    return results

@app.get("/")
def get_data():
    print('BEGIN')
    connection = mysql.connector.connect(host='localhost',
                                         database='batdongsandn',
                                         user='root',
                                         password='')
    print('BEGIN')

    query = 'SELECT * FROM databds'
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM databds")
    rows = cursor.fetchall()
    print('')

    result = []
    for datas in rows:
       title = datas[0]
       price = datas[1]
       description = datas[2]
       distCity = datas[3]
       uptime = datas[4]
       productArea = datas[5]

       print('##################')
       print(title)
       print(price)
       print(description)
       print(distCity)
       print(uptime)
       print(productArea)
       print('END')

       item = Item()
       item.title = title
       item.price = price
       item.description = description
       item.uptime = uptime
       item.distCity = distCity
       item.productArea = productArea
       result.append(item)


    return result


if __name__ == "__test__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


