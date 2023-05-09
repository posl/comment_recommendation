def main():
    n = input()
    while len(n) > 1:
        n = str(sum(map(int, n)))
    print('Yes' if n == '9' else 'No')
