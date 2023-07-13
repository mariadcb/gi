class Cancion:
    def __init__(self, nombre, duracion, artista):
        """
        Inicializa una nueva canción con un nombre, duración y artista.
        """
        self.nombre = nombre
        self.duracion = duracion
        self.artista = artista

class Artista:
    def __init__(self, nombre):
        """
        Inicializa un nuevo artista con un nombre.
        """
        self.nombre = nombre
        self.canciones = []

    def lanzar_cancion(self, cancion):
        """
        Agrega una canción a la lista de canciones del artista.
        """
        self.canciones.append(cancion)

class Usuario:
    def __init__(self, nombre):
        """
        Inicializa un nuevo usuario con un nombre.
        """
        self.nombre = nombre
        self.playlist = []
        self.artistas_seguidos = []

    def seguir_artista(self, artista):
        """
        Agrega un artista a la lista de artistas seguidos por el usuario.
        """
        self.artistas_seguidos.append(artista)

    def agregar_cancion_playlist(self, cancion):
        """
        Agrega una canción a la lista de reproducción del usuario.
        """
        self.playlist.append(cancion)

    def eliminar_cancion_playlist(self, cancion):
        """
        Elimina una canción de la lista de reproducción del usuario.
        """
        self.playlist.remove(cancion)

    def reproducir_cancion(self, cancion):
        """
        Simula la reproducción de una canción por parte del usuario.
        Ejemplo: Maxi está reproduciendo Bones de Imagine Dragons.
        """
        return f"{self.nombre} está reproduciendo {cancion.nombre} de {cancion.artista.nombre}"

    def escuchar_artista(self, artista):
        """
        Reproduce todas las canciones del artista si el usuario sigue al artista.
        Ejemplo: Maxi está escuchando todas las canciones de Imagine Dragons.
        Se reproduce cada una de las canciones luego de ese mensaje.
        Debe considerar el caso en el que el usuario no siga al artista y
        manejar ese caso individualmente.
        """
        if artista in self.artistas_seguidos:
            print(f"{self.nombre} está reproduciendo todas las canciones de {artista.nombre}")
            for cancion in artista.canciones:
                print(f"Ahora estas escuchando {cancion.nombre} de {cancion.artista.nombre} ")
        else:
            print("No seguis al artista.")


class AppMusica:
    def __init__(self, nombre):
        """
        Inicializa una nueva aplicación de música con un nombre.
        """
        self.nombre = nombre
        self.usuarios = []
        self.artistas = []
        self.canciones = []

    def agregar_usuario(self, usuario):
        """
        Agrega un usuario a la lista de usuarios de la aplicación.
        """
        self.usuarios.append(usuario)

    def agregar_artista(self, artista):
        """
        Agrega un artista a la lista de artistas de la aplicación.
        """
        self.artistas.append(artista)

    def agregar_cancion(self, cancion):
        """
        Agrega una canción a la lista de canciones de la aplicación.
        """
        self.canciones.append(cancion)

    def mostrar_usuarios(self):
        """
        Muestra todos los usuarios de la aplicación.
        """
        for usuario in self.usuarios:
            print(f"Usuario: {usuario.nombre}")

    def mostrar_artistas(self):
        """
        Muestra todos los artistas de la aplicación.
        """
        for artista in self.artistas:
            print(f"Artista: {artista.nombre}")

    def mostrar_canciones(self):
        """
        Muestra todas las canciones de la aplicación.
        """
        for cancion in self.canciones:
            print(f"Cancion: {cancion.nombre} de {cancion.artista.nombre}")

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
