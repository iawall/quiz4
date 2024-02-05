
class Square:
    def __init__(self, sideLength):
        self._sideLength = sideLength
    

    def getsideLength(self):
        return self._sideLength

    
    def getarea(self):
        return self._sideLength ** 2

def main():

    square = Square(sideLength = 10)

    print("Side Length is", square.getsideLength())
    print("Area is", square.getarea())


if __name__ == "__main__":
    main()
