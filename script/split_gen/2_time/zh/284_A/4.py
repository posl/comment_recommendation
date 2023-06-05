def solve():
    S = list(input())
    box = []
    for i in range(len(S)):
        if S[i] == "(":
            pass
        elif S[i] == ")":
            if len(box) > 0:
                box.pop()
            else:
                print("否")
                return
        else:
            box.append(S[i])
    if len(box) == 0:
        print("是")
    else:
        print("否")
    return
solve()
