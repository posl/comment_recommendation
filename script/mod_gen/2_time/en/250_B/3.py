def main():
    N, A, B = map(int, input().split())
    for i in range(A):
        for j in range(N):
            if j % 2 == 0:
                print((".#"*B)[:B], end="")
            else:
                print(("#."*B)[:B], end="")
        print()
    for i in range(N):
        for j in range(A):
            if i % 2 == 0:
                print((".#"*B)[:B], end="")
            else:
                print(("#."*B)[:B], end="")
        print()

if __name__ == '__main__':
    main()