def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 2
    print(count)
