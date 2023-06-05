def main():
    S = input()
    lenS = len(S)
    count = 0
    for i in range(lenS):
        for j in range(i,lenS):
            if int(S[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()