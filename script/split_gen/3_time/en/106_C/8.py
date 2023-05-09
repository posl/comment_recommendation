def  main():
    S = input()
    K = int(input())
    ans = 0
    for i in range(K):
        ans = int(S[i])
        if ans != 1:
            break
    print(ans)
