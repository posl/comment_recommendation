def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == '1':
            count += 1
    print(count*2 if count*2 < len(S) else len(S))

if __name__ == '__main__':
    main()