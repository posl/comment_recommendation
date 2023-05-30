def main():
    N = int(input())
    S = [input() for i in range(N)]
    if len(set(S)) == N:
        print("Yes")
    else:
        print("No")
main()
