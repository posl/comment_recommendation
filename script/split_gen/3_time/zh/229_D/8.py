def main():
    S = input()
    K = int(input())
    S = S.replace("X",".X.")
    S = S.split(".")
    ans = 0
    for s in S:
        ans = max(ans,len(s))
    print(ans-K)
