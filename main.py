import argparse

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("-a", type=int, help="an integer for the accumulator")
parser.add_argument("-b", type=int, help="an integer for the accumulator")
args = parser.parse_args()


def add_numbers(alpha, beta):
    return alpha + beta


def multiply_numbers(alpha, beta):
    return alpha * beta


if __name__ == "__main__":
    print("add_numbers: ", add_numbers(args.a, args.b))
    print("add_numbers: ", multiply_numbers(args.a, args.b))
