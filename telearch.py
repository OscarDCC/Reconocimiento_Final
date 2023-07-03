import requests

token = '6323074362:AAHeYmPOKxiRNoqYkKPpPr7L32pGZk_iUug'
chat_id = '1397290398'
chat_id_1 = '5407464083'
chat_id_2 = '5792975124'
chat_id_3 = '1383147762'
url = f"https://api.telegram.org/bot{token}/sendDocument"

file_path = '/home/jetson/prueba/Asistencia.xlsx'  # Ruta completa del archivo que deseas enviar

data = {'chat_id': chat_id}
data1 = {'chat_id_1': chat_id}
data2 = {'chat_id_2': chat_id}
data3 = {'chat_id_3': chat_id}
files = {'document': open(file_path, 'rb')}

response = requests.post(url, data=data, files=files)
response = requests.post(url, data=data1, files=files)
response = requests.post(url, data=data2, files=files)
response = requests.post(url, data=data3, files=files)

if response.status_code == 200:
    print("Archivo enviado")
else:
    print("Error al enviar el archivo:", response.text)

