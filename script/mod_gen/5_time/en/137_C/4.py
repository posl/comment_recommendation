def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    count = 0
    temp = 1
    for i in range(N-1):
        if S[i] == S[i+1]:
            temp += 1
        else:
            count += (temp*(temp-1))//2
            temp = 1
    count += (temp*(temp-1))//2
    print(count)

if __name__ == '__main__':
    main()