def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    if len(S) == N:
        print("Yes")
    else:
        print("No")
main()
