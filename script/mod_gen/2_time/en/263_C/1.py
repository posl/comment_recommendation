def print_sequences(n, m):
    if n == 1:
        for i in range(1, m + 1):
            print(i)
    else:
        for i in range(1, m + 1):
            print_sequences(n - 1, i - 1)
            for j in range(1, m + 1):
                print(i, end=" ")
            print()
n, m = map(int, input().split())
print_sequences(n, m)

if __name__ == '__main__':
    print_sequences()