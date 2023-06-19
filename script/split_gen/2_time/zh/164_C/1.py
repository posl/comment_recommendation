def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(len(set(S)))
main()
