class Song:
    """Class to represent a song.

     Attributes:
        title(str): song's title
        artist(str): name of artist responsible for representing song
        duration(int): duration of song, 0 if not specified
        """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent album using its tracks list.

    Attributes:
        name (str): the name of the album.
        year (int): the year was album released.
        artist (Artist): the artist responsible for album. If not
        specified the artist will be default to the 'Various Artists'.
        track [list(Song)]: a list of Songs on the Album

    Methods:
        add_song: use to add song to the Album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist('Various Artist')
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """adds song to a track list

        :param song: A song to add.
        :param position: optional an int if specified song will be added at
        int position. If not added in the end of track list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Class to store artist details:

    Attributes:
        name (str): name of the Artist:
        albums (List[Albums]): a list of Albums by this artist.

    Methods:
        add_albums: use to add albums to the artist's album list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Method to add album to the list.

        Attributes:
            album(str): album object to add to the list.
            if the album already exist in the list will not be added again.
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list


def create_checkfile(artist_list):
    with open('checkfile.txt', 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(f'{new_artist}\t{new_album}\t{new_song}', file=checkfile)




if __name__ == '__main__':
    artists = load_data()
    print(f'There are {len(artists)} artists.')

    create_checkfile(artists)