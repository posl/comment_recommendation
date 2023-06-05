def main():
    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(10**100):
        if i % 7 == 0:
            continue
        a = [[i*7+j for j in range(1, 8)] for _ in range(10**100)]
        for j in range(10**100):
            for k in range(7):
                if a[j][k] != b[j][k]:
                    break
            else:
                continue
            break
        else:
            print("Yes")
            exit()
    else:
        print("No")

if __name__ == '__main__':
    main()