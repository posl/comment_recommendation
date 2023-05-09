def main():
    S = input()
    K = int(input())
    l = len(S)
    for i in range(l):
        if S[i] != '1':
            print(S[i])
            break
        elif i == l-1:
            print(1)
