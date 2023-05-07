def main():
    S = list(input().split())
    T = list(input().split())
    if S == T:
        print('Yes')
        return
    if S[0] == S[1] and S[1] == S[2]:
        print('No')
        return
    if T[0] == T[1] and T[1] == T[2]:
        print('No')
        return
    print('Yes')
    return
main()
