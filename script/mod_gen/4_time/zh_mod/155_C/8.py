def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    count = 1
    max_count = 1
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
        else:
            count = 1
        if c

if __name__ == '__main__':
    main()