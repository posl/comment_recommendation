def main():
    S = input()
    #print(S)
    #print(len(S))
    count = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            #print(S[i:j])
            if int(S[i:j]) % 2019 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()