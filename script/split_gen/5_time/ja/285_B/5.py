def main():
    N = int(input())
    S = input()
    # print(N)
    # print(S)
    for i in range(1, N):
        # print(i)
        for l in range(1, N-i+1):
            # print(l)
            if S[l-1] == S[l-1+i]:
                break
        print(l-1)
