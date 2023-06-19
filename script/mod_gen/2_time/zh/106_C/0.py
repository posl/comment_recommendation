def main():
    S = input()
    K = int(input())
    cnt = 0
    for i in range(len(S)):
        if S[i] == '1':
            cnt += 1
        else:
            break
    if K <= cnt:
        print(1)
    else:
        print(S[cnt-1])

if __name__ == '__main__':
    main()