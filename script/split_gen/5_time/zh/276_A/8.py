def main():
    S = input()
    n = len(S)
    for i in range(n-1,-1,-1):
        if S[i] == 'a':
            print(i+1)
            exit()
    print(-1)
