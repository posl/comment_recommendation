def main():
    from builtins import int, map, list, print
    from sys import stdin, stdout
    # Read data
    a, b = map(int, stdin.readline().split())
    # Compute and print result
    result = 32**(a-b)
    stdout.write(str(result))

if __name__ == '__main__':
    main()