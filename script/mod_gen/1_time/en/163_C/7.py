def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    subordinates = [0] * (n+1)
    for i in range(2, n+1):
        subordinates[a[i-1]] += 1
    for i in range(1, n+1):
        print(subordinates[i])

if __name__ == '__main__':
    main()