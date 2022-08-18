import requests

#For listing products
endpoint = "http://127.0.0.1:8000/api/products/"

#For update, retrieve and delete products
endpoint = "http://127.0.0.1:8000/api/products/1/"

#For listing customers
endpoint = "http://127.0.0.1:8000/api/customers/"

#For update, retrieve and delete customer
endpoint = "http://127.0.0.1:8000/api/customers/1/"

#For customer registration
endpoint = "http://127.0.0.1:8000/api/register/"

get_response = requests.get(endpoint)
print(get_response.json())