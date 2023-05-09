def solve():
    S = input()
    T = input()
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        if S[i+1:] == T[i+1:]:
            print("Yes")
            return
        else:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    solve()