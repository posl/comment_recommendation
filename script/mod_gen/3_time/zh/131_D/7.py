def main():
    n = int(input())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append([a, b])
    ab.sort(key=lambda x: x[1])
    cur = 0
    for i in range(n):
        cur += ab[i][0]
        if cur > ab[i][1]:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()