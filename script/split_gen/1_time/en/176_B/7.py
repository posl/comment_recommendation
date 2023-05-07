def main():
    N = input()
    print('Yes' if sum(map(int, N)) % 9 == 0 else 'No')
