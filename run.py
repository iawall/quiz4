from moduleRoot.root import root
from moduleSquared.squared import squared
from moduleSum.sum import sums

def main():
    num = 5
    resultSum = sums(num)
    resultRoot = root(num)
    resultSquared = squared(num)
    print(resultSum)
    print(resultRoot)
    print(resultSquared)  


if __name__ == "__main__":
    main()

