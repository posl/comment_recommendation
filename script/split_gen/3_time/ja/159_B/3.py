def main():
    S = input()
    N = len(S)
    if S == S[::-1] and S[0:(N-1)//2] == S[0:(N-1)//2][::-1] and S[(N+3)//2-1:N] == S[(N+3)//2-1:N][::-1]:
        print("Yes")
    else:
        print("No")
