
class Square:
    def __init__(self, sideLength):
        self._sideLength = sideLength
    
    @property
    def sideLength(self):
        return self._sideLength

    @property
    def area(self):
        return self._sideLength ** 2

def main():

    square = Square(sideLength = 10)

    print("Side Length is", square.sideLength)
    print("Area is", square.area)


if __name__ == "__main__":
    main()


