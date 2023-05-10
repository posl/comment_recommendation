def solve():
    # 解答をここに書く
    A, B, C = map(int, input().split())
    if A == B:
        if A != C:
            print("Yes")
        else:
            print("No")
    elif A == C:
        if A != B:
            print("Yes")
        else:
            print("No")
    elif B == C:
        if A != B:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
