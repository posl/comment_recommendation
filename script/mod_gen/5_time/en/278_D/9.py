def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    q = int(input())
    b = [input().split() for _ in range(q)]
    for i in range(q):
        if b[i][0] == '1':
            a = [int(b[i][1]) for _ in range(n)]
        elif b[i][0] == '2':
            a[int(b[i][1])-1] += int(b[i][2])
        else:
            print(a[int(b[i][1])-1])
main()

if __name__ == '__main__':
    main()