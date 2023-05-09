def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[:N//2] == S[N//2:]:
            print(0)
        else:
            print(1)
    else:
        if S[:N//2] == S[N//2+1:]:
            print(1)
        else:
            print(2)
