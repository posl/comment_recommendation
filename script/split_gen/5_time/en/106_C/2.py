def main():
    S = input()
    K = int(input())
    for i in range(len(S)):
        if S[i] != '1':
            print(S[i])
            return
        elif i == K-1:
            print(S[i])
            return
