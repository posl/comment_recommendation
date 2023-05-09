def main():
    S = input()
    prev = S[0]
    count = 0
    for i in range(1,len(S)):
        if S[i] == prev:
            count += 1
        else:
            prev = S[i]
    print(count)

if __name__ == '__main__':
    main()