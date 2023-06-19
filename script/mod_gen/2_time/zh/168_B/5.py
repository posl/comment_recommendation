def main():
    K = int(input())
    S = input()
    if len(S) > K:
        print(S[0:K] + "...")
    else:
        print(S)

if __name__ == '__main__':
    main()