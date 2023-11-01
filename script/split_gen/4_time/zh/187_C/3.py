def main():
    N = int(input())
    s = set()
    for i in range(N):
        S = input()
        if S[0] == '!':
            if S[1:] in s:
                print(S[1:])
                return
            else
