import argparse, fibonacci


def fib(args):
    print(tuple(fibonacci.fibonacci(args.n)))


def parse_args():
    parser = argparse.ArgumentParser(description='Parser description.')
    subparsers = parser.add_subparsers()

    parser_fibonacci = subparsers.add_parser('fibonacci', help='Generate fibonacci sequence.')
    parser_fibonacci.add_argument('n', type=int, help='Generate up to n.')
    parser_fibonacci.set_defaults(func=fib)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
