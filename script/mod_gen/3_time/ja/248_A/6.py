def main():
    S = input()
    S = list(S)
    S = list(map(int,S))
    S.sort()
    for i in range(1,10):
        if i not in S:
            print(i)
            break

if __name__ == '__main__':
    main()