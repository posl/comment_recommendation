def main():
    n, m = map(int, input().split())
    x = []
    for i in range(m):
        x.append(list(map(int, input().split()))[1:])
    for i in range(n):
        for j in range(i+1, n):
            if not any([i+1 in xi for xi in x]):
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()