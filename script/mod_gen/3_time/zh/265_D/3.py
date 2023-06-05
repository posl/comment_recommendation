def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, P, Q, R)
    # print(A)
    # print(sum(A))
    # print(P+Q+R)
    if sum(A) == P+Q+R:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()