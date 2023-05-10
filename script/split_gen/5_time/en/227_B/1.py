def main():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    if S[0] + S[1] + S[2] == S[3] + S[4]:
        print(2)
    elif S[0] + S[1] + S[2] + S[3] == S[4]:
        print(1)
    else:
        print(0)
