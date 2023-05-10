def main():
    n, x = map(int, input().split())
    alc = 0
    for i in range(n):
        v, p = map(int, input().split())
        alc += v * p
        if alc > x * 100:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()