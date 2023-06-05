def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "0":
            ans += 1
    print(ans)
