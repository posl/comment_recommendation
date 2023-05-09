def main():
    S = input()
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == 'R':
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