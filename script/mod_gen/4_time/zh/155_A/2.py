def solve():
    A,B,C = map(int,input().split())
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()