def main():
    n = int(input())
    a = [0] * 1000000
    for i in range(n):
        s, t = map(int, input().split())
        a[s - 1] += 1
        a[t] -= 1
    for i in range(1, 1000000):
        a[i] += a[i - 1]
    print(sum(a))

if __name__ == '__main__':
    main()