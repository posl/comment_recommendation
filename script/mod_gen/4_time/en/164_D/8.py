def main():
    S = input()
    #print(S)
    s = [int(i) for i in S]
    #print(s)
    l = len(S)
    #print(l)
    #print('i, j, s[i-1:j]')
    count = 0
    for i in range(1, l+1):
        for j in range(i, l+1):
            #print(i, j, s[i-1:j])
            if int(S[i-1:j]) % 2019 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()