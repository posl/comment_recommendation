def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    temp = S[0]
    max = 0
    count = 0
    for i in range(N):
        if S[i] == temp:
            count += 1
        else:
            if count > max:
                max = count
                result = temp
            temp = S[i]
            count = 1
    if count > max:
        result = temp
    print(result)

if __name__ == '__main__':
    main()