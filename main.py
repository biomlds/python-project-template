import argparse
from os import listdir

from functions import add_numbers, multiply_numbers

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("-a", type=int, help="an integer for the accumulator")
parser.add_argument("-b", type=int, help="an integer for the accumulator")
args = parser.parse_args()


print(multiply_numbers(2, 3))


print(listdir())

if __name__ == "__main__":
    print("add_numbers: ", add_numbers(args.a, args.b))
    print("multiply_numbers: ", multiply_numbers(args.a, args.b))
