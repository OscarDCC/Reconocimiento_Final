import requests

token = '6323074362:AAHeYmPOKxiRNoqYkKPpPr7L32pGZk_iUug'

url = f"https://api.telegram.org/bot{token}/sendDocument"

file_path = '/home/jetson/Reconocimiento_Final/Asistencia.xlsx'  # Ruta completa del archivo que deseas enviar

chat_id_cero = '1397290398'
datacero = {'chat_id': chat_id_cero}
files = {'document': open(file_path, 'rb')}
response = requests.post(url, data=datacero, files=files)

if response.status_code == 200:
    print("Archivo enviado")
else:
    print("Error al enviar el archivo:", response.text)

chat_id_cero = '5407464083'
datacero = {'chat_id': chat_id_cero}
files = {'document': open(file_path, 'rb')}
response = requests.post(url, data=datacero, files=files)

if response.status_code == 200:
    print("Archivo enviado")
else:
    print("Error al enviar el archivo:", response.text)

chat_id_cero = '5792975124'
datacero = {'chat_id': chat_id_cero}
files = {'document': open(file_path, 'rb')}
response = requests.post(url, data=datacero, files=files)

if response.status_code == 200:
    print("Archivo enviado")
else:
    print("Error al enviar el archivo:", response.text)

chat_id_cero = '1383147762'
datacero = {'chat_id': chat_id_cero}
files = {'document': open(file_path, 'rb')}
response = requests.post(url, data=datacero, files=files)

if response.status_code == 200:
    print("Archivo enviado")
else:
    print("Error al enviar el archivo:", response.text)

