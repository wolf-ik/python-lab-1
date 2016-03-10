import argparse, fibonacci, sort, storage, wordcount


def fibonacci_handler(args):
    print(tuple(fibonacci.fibonacci(args.n)))


def my_sort_handler(args):
    array = map(int, args.array.split(' '))
    print(sort.sort_handler(array, method=args.method))


def storage_handler(args):
    strg = storage.Storage()
    strg.run()


def word_count_handler(args):
    with open(args.filename, 'r') as f:
        k, n = args.k, args.n
        wc = wordcount.WordCount(str(f.read()))
        for key, value in wc.get_words():
            print('{}: {}'.format(key, value))
        print('*************')
        print('Average words in sentence: %f' % wc.get_average_words())
        print('Median: %s - %d' % wc.get_median())
        print('*************')
        print('Top {} {}-gramm:'.format(k, n))
        for key, value in wc.n_gramm(k, n):
            print('{}: {}'.format(key, value))


def parse_args():
    parser = argparse.ArgumentParser(description='My wonderful description.')
    subparsers = parser.add_subparsers()

    parser_fibonacci = subparsers.add_parser('fibonacci', help='Generate fibonacci sequence.')
    parser_fibonacci.add_argument('n', type=int, help='Generate up to n.')
    parser_fibonacci.set_defaults(func=fibonacci_handler)

    parser_sort = subparsers.add_parser('sort', help='Sort array.')
    parser_sort.add_argument('-m', '--method', type=str, help='Methods: radix, quick, merge.')
    parser_sort.add_argument('array', type=str, help='Input array.')
    parser_sort.set_defaults(func=my_sort_handler)

    parser_storage = subparsers.add_parser('storage', help='Interactive storage.')
    parser_storage.set_defaults(func=storage_handler)

    parser_word_count = subparsers.add_parser('wc', help='Word count.')
    parser_word_count.add_argument('filename', type=str, help='Path to input file.')
    parser_word_count.add_argument('k', type=int, help='Top K N-gramm.')
    parser_word_count.add_argument('n', type=int, help='Length N-gramm.')
    parser_word_count.set_defaults(func=word_count_handler)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
