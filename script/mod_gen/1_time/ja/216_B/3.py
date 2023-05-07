def main():
    n = int(input())
    for i in range(n):
        si, ti = input().split()
        for j in range(i+1, n):
            sj, tj = input().split()
            if si == sj and ti == tj:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()