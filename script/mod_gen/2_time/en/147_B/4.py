def main():
    S = input()
    L = len(S)
    count = 0
    for i in range(L//2):
        if S[i] != S[L-i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()