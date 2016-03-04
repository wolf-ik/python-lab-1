import argparse, fibonacci, sort, storage


def fibonacci_handler(args):
    print(tuple(fibonacci.fibonacci(args.n)))


def my_sort_handler(args):
    array = map(int, args.array.split(' '))
    print(sort.sort_handler(array, method=args.method))


def storage_handler(args):
    strg = storage.Storage()
    strg.run()


def parse_args():
    parser = argparse.ArgumentParser(description='Parser description.')
    subparsers = parser.add_subparsers()

    parser_fibonacci = subparsers.add_parser('fibonacci', help='Generate fibonacci sequence.')
    parser_fibonacci.add_argument('n', type=int, help='Generate up to n.')
    parser_fibonacci.set_defaults(func=fibonacci_handler)

    parser_sort = subparsers.add_parser('sort', help='Sort array.')
    parser_sort.add_argument('method', type=str, help='Methods: radix, quick, merge.')
    parser_sort.add_argument('array', type=str, help='Input array.')
    parser_sort.set_defaults(func=my_sort_handler)

    parser_storage = subparsers.add_parser('storage', help='Interaktive storage.')
    parser_storage.set_defaults(func=storage_handler)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
