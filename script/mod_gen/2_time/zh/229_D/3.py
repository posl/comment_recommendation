def main():
    S = input()
    K = int(input())
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "X":
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    if max < count:
        max = count
    if K == 0:
        print(max)
        return
    if max + K > len(S):
        print(len(S))
        return
    print(max + K)

if __name__ == '__main__':
    main()