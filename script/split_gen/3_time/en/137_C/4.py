def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    ans = 0
    count = 1
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            ans += int(count * (count-1) / 2)
            count = 1
    ans += int(count * (count-1) / 2)
    print(ans)
