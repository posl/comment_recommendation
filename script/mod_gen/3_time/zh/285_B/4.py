def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        while i + l < N and S[l] != S[i + l]:
            l += 1
        print(l)
main()
