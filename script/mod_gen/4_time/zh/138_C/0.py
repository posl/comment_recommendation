def main():
    n = int(input())
    vl = list(map(int, input().split()))
    vl.sort()
    res = vl[0]
    for i in range(1, n):
        res = (res + vl[i]) / 2
    print(res)

if __name__ == '__main__':
    main()