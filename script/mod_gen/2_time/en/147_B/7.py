def main():
    S = input()
    S = S[::-1]
    count = 0
    for i in range(len(S)):
        if S[i] != S[-i-1]:
            count += 1
    print(count//2)
main()

if __name__ == '__main__':
    main()