def main():
    P = input().split()
    print(P)
    for i in range(len(P)):
        P[i] = int(P[i])
    print(P)
    ans = ""
    for i in range(26):
        ans += chr(P[i] + 96)
    print(ans)
