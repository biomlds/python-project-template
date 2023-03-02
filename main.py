import argparse

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("-a", type=int, help="an integer for the accumulator")
parser.add_argument("-b", type=int, help="an integer for the accumulator")

args = parser.parse_args()


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    res1 = add_numbers(args.a, args.b)
    print(res1)
