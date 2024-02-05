import argparse

def parse() -> None: #returning nothing\
    
    parser = argparse.ArgumentParser()
    parser.add_argument("instring",help="Enter a string",type=str)
    parser.add_argument("innum",help="Enter an integer",type=int)
    parser.add_argument("infloat",help="Enter a floating number",type=float)

    args = parser.parse_args()

    print(f'String: {args.instring}')
    print(f'Integer: {args.innum}')
    print(f'Float: {args.infloat}')

if __name__ == "__main__":
    parse()