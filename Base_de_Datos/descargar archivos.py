import requests

# Función para descargar un archivo
def descargar_archivo(url, nombre_archivo):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)
        print(f'Archivo {nombre_archivo} descargado con éxito.')
    else:
        print(f'Error al descargar el archivo {nombre_archivo}.')

# URL base
url_base = 'https://archive.physionet.org/atm/edb/'

# Iterar desde e0103 hasta e1304
for i in range(103, 1305):
    codigo = f'e{i:04}'  # Formatear el número a 4 dígitos con ceros a la izquierda
    url_completa = f'{url_base}{codigo}/atr/0/e/rr/t/rr.txt'
    nombre_archivo = f'{codigo}.txt'
    descargar_archivo(url_completa, nombre_archivo)
