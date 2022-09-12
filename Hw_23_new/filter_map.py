import requests

url = "http://127.0.0.1:5000/perform_query"

payload={
  'file_name': 'apache_logs.txt',
  'cmd1': 'filter',
  'value1': 'image',
  'cmd6': 'filter',
  'value6': '304',
  'cmd3': 'map',
  'value3': '1',
  'cmd5': 'unique',
  'value5': '',
  'cmd2': 'sort',
  'value2': 'asc',
  'cmd4': 'limit',
  'value4': 10
}

response = requests.request("POST", url, data=payload)
print(response.text)
