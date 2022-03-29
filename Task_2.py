import requests
r = requests.get("https://www.google.com")
print(r.headers)
try:
    print('Server: '+ r.headers['Server'])
except:
    print('Information not available')
try:
    print('Date: ' + r.headers['Date'])
except:
    print('Information not available')
try:
    print(r.headers['X-Country_Code'])
except:
    print('X-Country_Code: '+'Information not available')
try:
    print(r.headers['Connection'])
except:
    print('Connection' + 'Information not available')
try:
    print(r.headers['Content-Length'])
except:
    print('Content-Length' + 'Information not available')


