def main():
    S = input()
    K = int(input())
    if len(S) >= K:
        print(S[K-1])
        return
    for i in range(len(S)):
        if int(S[i]) > 1:
            print(S[i])
            return
    print(1)
main()

if __name__ == '__main__':
    main()