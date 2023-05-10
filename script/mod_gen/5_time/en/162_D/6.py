def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if S[i] != S[j]:
                for k in range(j+1, N):
                    if S[i] != S[k] and S[j] != S[k] and j-i != k-j:
                        count += 1
    print(count)

if __name__ == '__main__':
    main()