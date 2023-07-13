from appmusica import *
from usuario import *
from artista import *
from cancion import *


#ARTISTA 1
artista1 = Artista("Imagine Dragons")
cancion1 = Cancion("Bones", 90, artista1)
cancion2 = Cancion("X", 190, artista1)

artista1.lanzar_cancion(cancion1)
artista1.lanzar_cancion(cancion2)

#ARTISTA 2
artista2 = Artista("Fito Paez")
cancion3 = Cancion("Mariposa T.", 890, artista2)
cancion4 = Cancion("Amor", 390, artista2)

#Usuarios
usuario1 = Usuario("Ramiro")
usuario2 = Usuario("Matias")

#APP_MUSICA
app_musica = AppMusica("Spotify del norte")

app_musica.agregar_artista(artista1)
app_musica.agregar_artista(artista2)

app_musica.agregar_usuario(usuario1)
app_musica.agregar_usuario(usuario2)

app_musica.agregar_cancion(cancion1)
app_musica.agregar_cancion(cancion2)
app_musica.agregar_cancion(cancion3)
app_musica.agregar_cancion(cancion4)

usuario1.seguir_artista(artista1)
usuario1.agregar_cancion_playlist(cancion1)
usuario1.agregar_cancion_playlist(cancion2)

play = usuario1.reproducir_cancion(cancion1)
print(play)
#usuario1.eliminar_cancion_playlist(cancion1)

usuario1.escuchar_artista(artista1)