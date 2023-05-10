def main():
    n, m = map(int, input().split())
    b = []
    for i in range(n):
        b.append(list(map(int, input().split())))
    c = []
    for i in range(10**100):
        c.append([i*7+1, i*7+2, i*7+3, i*7+4, i*7+5, i*7+6, i*7+7])
    for i in range(10**100):
        if b[0] == c[i]:
            for j in range(n):
                if b[j] != c[i+j]:
                    print("No")
                    exit()
            print("Yes")
            exit()
    print("No")
main()
