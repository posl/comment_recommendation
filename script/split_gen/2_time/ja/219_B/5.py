def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    S = [S1, S2, S3]
    ans = ""
    for i in range(len(T)):
        ans += S[int(T[i]) - 1]
    print(ans)
