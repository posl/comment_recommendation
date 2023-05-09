def main():
    S = input()
    mod = 2019
    count = 0
    for i in range(len(S)):
        for j in range(i+1,len(S)+1):
            num = int(S[i:j])
            if num % mod == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()