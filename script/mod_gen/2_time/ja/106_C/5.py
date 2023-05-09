def main():
    S = input()
    K = int(input())
    count = 0
    for i in range(K):
        if S[i] == '1':
            count += 1
        else:
            print(S[i])
            break
        if count == K:
            print(1)

if __name__ == '__main__':
    main()