def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(0)
    for i in a:
        b[i-1] += 1
    for i in b:
        print(i)

if __name__ == '__main__':
    main()