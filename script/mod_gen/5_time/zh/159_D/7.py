def main():
    n = int(input())
    a = [0] * n
    for i, x in enumerate(map(int, input().split())):
        a[x - 1] += 1
    s = sum(x * (x - 1) // 2 for x in a)
    for x in a:
        print(s - x * (x - 1) // 2 + (x - 1) * (x - 2) // 2)

if __name__ == '__main__':
    main()