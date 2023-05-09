def main():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    if S[-1] < sum(S[:-1]):
        print("Yes")
    else:
        print("No")
