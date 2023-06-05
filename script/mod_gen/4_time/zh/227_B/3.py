def main():
    N = int(input())
    S = list(map(int, input().split()))
    #print(N)
    #print(S)
    count = 0
    for s in S:
        if s == 1:
            count += 1
        else:
            for i in range(2,s):
                if s%i == 0:
                    count += 1
                    break
    print(N-count)

if __name__ == '__main__':
    main()