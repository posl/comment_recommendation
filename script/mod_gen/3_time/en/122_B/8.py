def main():
    S = input()
    s = "ACGT"
    count = 0
    max = 0
    for i in range(len(S)):
        if S[i] in s:
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)
main()

if __name__ == '__main__':
    main()