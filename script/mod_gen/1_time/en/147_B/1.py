def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] != S[-i-1]:
            count += 1
    print(int(count/2))

if __name__ == '__main__':
    main()