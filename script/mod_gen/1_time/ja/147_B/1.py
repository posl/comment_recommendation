def main():
    S = input()
    cnt = 0
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()