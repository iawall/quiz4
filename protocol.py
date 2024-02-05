from typing import Protocol, Any

class BallProtocol(Protocol):

    def save(self, data: Any) -> None:
        ...

    def load(self) -> None:
        ...

class Ball(BallProtocol):

    def save(self, data: Any) -> None:
        pass

    def load(self) -> None:
        pass

class Football(Ball):

    def __init__(self, color: str, material: str):
        self.color = color
        self.material = material

    def display(self) -> None:
        print(f"Football - Color: {self.color}, Material: {self.material}")

    def save(self, data: Any) -> None:
        print(f"Saving Football data: {data}")

    def load(self) -> None:
        print("Loading Football data")

class Baseball(Ball):

    def __init__(self, diameter: float, stitching: str):
        self.diameter = diameter
        self.stitching = stitching

    def display(self) -> None:
        print(f"Baseball - Diameter: {self.diameter}, Stitching: {self.stitching}")

    def save(self, data: Any) -> None:
        print(f"Saving Baseball data: {data}")

    def load(self) -> None:
        print("Loading Baseball data")

def main() -> None:
    
    football = Football(color="brown", material="rubber")
    baseball = Baseball(diameter=2.94, stitching="red")

    football.display()
    football.save("Football-specific data")
    football.load()

    baseball.display()
    baseball.save("Baseball-specific data")
    baseball.load()

if __name__ == "__main__":
    main()
