def main():
    S = input()
    K = int(input())
    count = 0
    for i in range(len(S)):
        if S[i] == '1':
            count += 1
        else:
            break
    if K <= count:
        print(1)
    else:
        print(S[count])

if __name__ == '__main__':
    main()