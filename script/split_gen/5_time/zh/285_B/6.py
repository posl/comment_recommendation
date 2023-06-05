def main():
    N = int(input())
    S = input()
    ans = []
    for i in range(1, N):
        l = 0
        while i + l < N:
            if S[l] != S[i + l]:
                l += 1
            else:
                break
        ans.append(l)
    print("\n".join(map(str, ans)))
