def main():
    S = input()
    T = input()
    ans = len(T)
    for i in range(len(S) - len(T) + 1):
        cnt = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)
main()
The code is self-explanatory. I just iterate through all possible positions of T in S and count the number of characters that need to be changed. The minimum of these is the answer.
