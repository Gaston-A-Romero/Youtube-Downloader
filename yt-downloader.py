#Para utilizar debemos instalar la libreria pytube y tqdm utilizando el comando : { pip install pytube & pip install tqdm } en nuestra terminal

from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
import os
import __main__
from tqdm import tqdm

#Funcion para comprobar si hay una carpeta donde se almacenan las descargas
def existe_carpeta_descarga(ruta):
    if not os.path.exists('.\\Descargas'):
        os.mkdir('.\\Descargas')
        print('Se creo una carpeta para guardar todas sus descargas en la ruta: ', os.path.abspath('.\\Descargas'))
    
def main():   
    archivo_path = os.path.abspath(__main__.__file__)
    existe_carpeta_descarga(archivo_path)
    canciones_no_descargadas = []

    #Menu de opciones
    opcion = -1
    while not 1 <= opcion <= 3:

        print('*'*50)
        print('Menu')
        print('1-Descargar audio de un video')
        print('2-Descargar video')
        print('3-Descargar todos los audios de una playlist')
        print('*'*50)

        opcion = int(input('Ingrese el numero de la tarea a realizar: '))

    #Opcion para descargar audio de un video individual
    if opcion == 1:
        url = input('Ingrese link del video: ')
        #Creando el objeto de la libreria que nos trae los datos sobre el video
        yt = YouTube(url,on_progress_callback=on_progress)
        audio = yt.streams.get_audio_only()
        audio_size_archivo = audio.filesize_mb
        try:          
            audio.download(output_path='Descargas')             
            print('Su audio fue descargado con exito y se encuentra en la carpeta descargas :)')
        except:
            print('Ocurrio un error. Vuelva a intentar...')
        
        print("*"*50)
        

    #Opcion para descargar un video    
    elif opcion == 2:
        url = input('Ingrese link del video: ')
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        try:
            video.download(output_path='Descargas')
        except:
            print('No se pudo descargar el video. Intente nuevamente')

        print("*"*50)
        print("Descarga finalizada...")

    #Opcion para descargar una lista publica de canciones
    elif opcion == 3:
        print('Tener en cuenta que la playlist debe estar publica para poder descargarse'.upper())
        url = input('Ingrese el link de la playlist de musica para descargar: ')
        
        yt = Playlist(url)
        print(yt.length)
        url_videos = yt.video_urls
        for i in tqdm(range(yt.length),unit='canciones',desc='Descargando',unit_scale=True,write_bytes=False):
            try:                
                yt = YouTube(url_videos[i])
                cancion = yt.streams.get_audio_only()
                cancion.download(output_path='Descargas')
            except:
                print('No se pudo descargar la cancion con el link: ',url_videos[i])
                canciones_no_descargadas.append(url_videos[i])
                print('Pruebe descargando dicha cancion con la opcion 1 del programa')

        #Devuelvo las canciones que no se pudieron descargar      
        if len(canciones_no_descargadas) > 0:
                    print('Las siguientes canciones no fueron descargadas')
                    for i in canciones_no_descargadas:
                        print(canciones_no_descargadas[i])

        print("*"*50)
        print("Descarga finalizada...")

if __name__ == '__main__':
    main()