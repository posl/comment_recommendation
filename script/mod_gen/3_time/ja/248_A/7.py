def main():
    S = input()
    S = list(S)
    S = list(map(int, S))
    for i in range(10):
        if i not in S:
            print(i)
            exit()

if __name__ == '__main__':
    main()