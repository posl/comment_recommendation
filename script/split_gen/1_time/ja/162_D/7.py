def main():
    N = int(input())
    S = input()
    rgb = [0, 0, 0]
    for c in S:
        if c == "R":
            rgb[0] += 1
        elif c == "G":
            rgb[1] += 1
        elif c == "B":
            rgb[2] += 1
    ans = rgb[0] * rgb[1] * rgb[2]
    for i in range(N):
        for j in range(i + 1, N):
            k = j + (j - i)
            if k >= N:
                break
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)
