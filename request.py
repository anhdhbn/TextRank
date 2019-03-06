import requests

sample_file = open("data/docs/vi/test.txt", 'r')
text = sample_file.read()

url = 'http://localhost:5000/api/execute'
r = requests.post(url,json={
    'text':text,
    'lang':'vi',
    'ratio' : 0.2
    })
print(r.json())