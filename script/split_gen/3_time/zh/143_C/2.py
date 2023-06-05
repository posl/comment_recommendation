def main():
    N = int(input())
    S = input()
    S = list(S)
    S.append(' ')
    count = 0
    for i in range(N):
        if S[i] != S[i + 1]:
            count += 1
    print(count)
