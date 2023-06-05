def main():
    S = input()
    K = int(input())
    n = len(S)
    S = S + S
    start = 0
    end = 0
    cnt = 0
    ans = 0
    for i in range(n):
        if S[i] == "X":
            end += 1
        else:
            if cnt < K:
                end += 1
                cnt += 1
            else:
                while S[start] == "X":
                    start += 1
                start += 1
                end += 1
        ans = max(ans, end - start)
    print(ans)
