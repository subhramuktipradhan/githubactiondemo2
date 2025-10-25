from urllib import response
import requests
import pandas as pd

data=requests.get("https://jsonplaceholder.typicode.com/users")
j=response.json(data)
df=pd.DataFrame(j)