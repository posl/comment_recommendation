def main():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    print(min(b) - max(a) + 1 if min(b) - max(a) + 1 > 0 else 0)

if __name__ == '__main__':
    main()