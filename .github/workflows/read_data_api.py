import requests

import pandas as pd
import response

data=requests.get("https://jsonplaceholder.typicode.com/users")
j=response.json
df=pd.DataFrame(j)