def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if i == 0:
            continue
        if S[i-1] != S[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()