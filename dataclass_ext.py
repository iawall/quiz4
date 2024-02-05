from dataclasses import dataclass

@dataclass
class Song:
    title: str
    artist: str
    genre: str
    release_year: int
    number_of_streams: int
    monthly_listeners: int

    def display_info(self):

        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Genre: {self.genre}")
        print(f"Release Year: {self.release_year}")
        print(f"Number of Streams: {self.number_of_streams}")
        print(f"Monthly Listeners: {self.monthly_listeners}")

    def estimate_streams_per_year(self) -> float:

        current_year = 2024
        years_since_release = current_year - self.release_year
        return self.number_of_streams / years_since_release 

def main():
    song1 = Song(title="Let It Happen", artist="Tame Impala", genre="Psych Rock", release_year=2015, number_of_streams=491028980, monthly_listeners=26500000)

    song2 = Song(title="Moving Out", artist="Vacations", genre="Pop", release_year=2018, number_of_streams=14755880, monthly_listeners=10700000)

    song1.display_info()

    estimated_streams1 = song1.estimate_streams_per_year()
    print(f"Estimated Streams Per Year: {estimated_streams1:.2f}")
    print("\n")

    song2.display_info()
    
    estimated_streams2 = song2.estimate_streams_per_year()
    print(f"Estimated Streams Per Year: {estimated_streams2:.2f}")

if __name__ == "__main__":
    main()
