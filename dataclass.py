
from dataclasses import dataclass

@dataclass
class Song:
    
    title: str
    artist: str
    genre: str
    release_year: int


    def display_info(self):

        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Genre: {self.genre}")
        print(f"Release Year: {self.release_year}")

def main():
    
    song1 = Song(title="Let It Happen", artist="Tame Impala", genre="Psych Rock", release_year=2015)

    song2 = Song(title="Moving Out", artist="Vacations", genre="Pop", release_year=2018)

    song1.display_info()

    print("\n")

    song2.display_info()

if __name__ == "__main__":
    main()
