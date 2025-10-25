import requests

import pandas as pd
import response

data=requests.get("https://jsonplaceholder.typicode.com/users")
j=response.json(data)
df=pd.DataFrame(j)