def main():
    S = input()
    T = input()
    count = 0
    for i in range(0,len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()