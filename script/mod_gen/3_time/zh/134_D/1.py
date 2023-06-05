def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[i] = (a[i] + sum(b[i::i+1])) % 2
    print(sum(b))
    print(*[i+1 for i in range(n) if b[i]])

if __name__ == '__main__':
    main()