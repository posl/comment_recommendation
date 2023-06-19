def main():
    S = input()
    K = int(input())
    num = 0
    for i in range(len(S)):
        if S[i] == '1':
            num += 1
        else:
            break
    if K <= num:
        print(1)
    else:
        print(S[num - 1])

if __name__ == '__main__':
    main()