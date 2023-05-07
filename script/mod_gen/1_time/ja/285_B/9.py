def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        #print(i)
        result = 0
        for j in range(1, N - i + 1):
            if S[j - 1] != S[j + i - 1]:
                result += 1
            else:
                break
        print(result)

if __name__ == '__main__':
    main()