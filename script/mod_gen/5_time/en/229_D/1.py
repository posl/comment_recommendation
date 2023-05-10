def main():
    S = input()
    K = int(input())
    count = 0
    if S[0] == 'X':
        count = 1
    for i in range(1, len(S)):
        if S[i] == 'X':
            if S[i-1] == 'X':
                count += 1
            else:
                count = 1
        else:
            if count > 0:
                if K > 0:
                    count += 1
                    K -= 1
                else:
                    count = 0
    print(count)
main()

if __name__ == '__main__':
    main()