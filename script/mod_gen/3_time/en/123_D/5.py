def solve():
    X, Y, Z, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    ABC = []
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for ans in ABC[:K]:
        print(ans)

if __name__ == '__main__':
    solve()