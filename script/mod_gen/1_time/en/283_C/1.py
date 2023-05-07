def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if i == 0:
            count += 1
        elif S[i] != "0":
            count += 2
    print(count)

if __name__ == '__main__':
    main()