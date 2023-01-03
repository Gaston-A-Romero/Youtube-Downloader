#Para utilizar debemos instalar la libreria pytube utilizando el comando : { pip install pytube } en nuestra terminal

from pytube import YouTube
from pytube import Playlist
import os
import __main__

def existe_carpeta_descarga(ruta):
    if os.path.exists('.\\Descargas') == False:
        os.mkdir('.\\Descargas')
        print('Se creo una carpeta para guardar todas sus descargas en la ruta: ', os.path.abspath('.\\Descargas'))
    
def main():   
    archivo_path = os.path.abspath(__main__.__file__)
    existe_carpeta_descarga(archivo_path)
    
    opcion = -1
    while not 1 <= opcion <= 3:

        print('*'*50)
        print('Menu')
        print('1-Descargar audio de un video')
        print('2-Descargar video')
        print('3-Descargar todos los audios de una playlist')
        print('*'*50)

        opcion = int(input('Ingrese el numero de la tarea a realizar: '))


    if opcion == 1:
        url = input('Ingrese link del video: ')
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()
        try:
            audio.download(output_path='Descargas')
            print('Su audio fue descargado con exito y se encuentra en la carpeta descargas :)')
        except:
            print('Ocurrio un error. Vuelva a intentar...')
        
        print("*"*50)
        print("Descarga finalizada...")

        
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

    elif opcion == 3:
        print('Tener en cuenta que la playlist debe estar publica para poder descargarse')
        url = input('Ingrese el link de la playlist de musica para descargar: ')
        yt = Playlist(url)
        url_videos = yt.video_urls
        for i in range(yt.length):
            try:                
                yt = YouTube(url_videos[i])
                cancion = yt.streams.get_audio_only()
                cancion.download(output_path='Descargas')
            except:
                print('No se pudo descargar la cancion con el link: ',url_videos[i])
                print('Pruebe descargando dicha cancion con la opcion 1 del programa')


        print("*"*50)
        print("Descarga finalizada...")

if __name__ == '__main__':
    main()