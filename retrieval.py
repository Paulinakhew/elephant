# install the requests package using 'pip3 install requests'
import requests

response = requests.post('https://api.td-davinci.com/api/raw-customer-data',
    headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiNjljZDEyYmItMDlkYy0zNjc4LWJlNWYtZGExNmNjY2U3MjRjIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiIwYWVjMTI3ZS1hZmU0LTQ3ZWItOTQ1My0zOTM4MjRlNjJjMjQifQ.thFjT6PaKBJ7XT4IYXWNsHeT_rlsXoNY5oYb0uQH5JA' })
response_data = response.json()

customer_id = []

for r in response_data['result']['customers']['id']:
    print(r)

# print(response_data['result'])