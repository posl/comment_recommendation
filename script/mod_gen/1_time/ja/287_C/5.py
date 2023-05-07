def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    else:
        for i in range(m):
            u, v = map(int, input().split())
            if abs(u - v) != 1:
                print("No")
                return
        print("Yes")

if __name__ == '__main__':
    main()