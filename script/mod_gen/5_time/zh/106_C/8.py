def main():
    S = input()
    K = int(input())
    for i in range(K):
        if S[i] != "1":
            print(S[i])
            return
    print("1")

if __name__ == '__main__':
    main()