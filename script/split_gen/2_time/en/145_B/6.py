def main():
    N = int(input())
    S = input()
    for i in range(N//2):
        if S[i] != S[i+N//2]:
            print('No')
            return
    print('Yes')
