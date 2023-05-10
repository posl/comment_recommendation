def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    for pi in p:
        if sum(pi) < k*3:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()