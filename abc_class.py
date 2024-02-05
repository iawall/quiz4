from abc import ABC, abstractmethod

class Ball(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass

class Football(Ball):
    
    def __init__(self, color, material):
        self.color = color
        self.material = material

    def display(self):
        print(f"Football - Color: {self.color}, Material: {self.material}")

    def save(self, data):
        print(f"Saving Football data: {data}")

    def load(self):
        print("Loading Football data")

class Baseball(Ball):

    def __init__(self, diameter, stitching):
        self.diameter = diameter
        self.stitching = stitching

    def display(self):
        print(f"Baseball - Diameter: {self.diameter}, Stitching: {self.stitching}")

    def save(self, data):
        print(f"Saving Baseball data: {data}")

    def load(self):
        print("Loading Baseball data")

def main():

    football = Football(color="brown", material="rubber")
    baseball = Baseball(diameter=2.94, stitching="red")

    football.display()
    football.save("Football data")
    football.load()

    baseball.display()
    baseball.save("Baseball data")
    baseball.load()

if __name__ == "__main__":
    main()
