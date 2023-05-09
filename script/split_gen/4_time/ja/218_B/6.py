def main():
    P = list(map(int,input().split()))
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    ans = ""
    for i in range(len(P)):
        ans += alphabets[P[i]-1]
    print(ans)
