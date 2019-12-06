author = 'Arya Santri'
email = 'aryawiratama@gmail.com'
app_title = 'Menggunakan Python Request Untuk Memanggil Django API'
print(f'{app_title} oleh {author}')

# Memanggil API di Server Django
url = 'http://127.0.0.1:8000/'
import requests

response = requests.get(url)
print(response)

#pastikan <Response [200]> => Succes!, [300/400/500] => Error
