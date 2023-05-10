def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    lr = [list(map(int, input().split())) for _ in range(q)]
    for i in range(q):
        l = lr[i][0]
        r = lr[i][1]
        x = lr[i][2]
        print(a[l-1:r].count(x))

if __name__ == '__main__':
    main()