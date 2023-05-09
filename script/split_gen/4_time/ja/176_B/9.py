def main():
    n = input()
    n = list(n)
    n = list(map(int, n))
    if sum(n) % 9 == 0:
        print('Yes')
    else:
        print('No')
