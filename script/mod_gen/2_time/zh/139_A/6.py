def main():
    S = input()
    T = input()
    result = 0
    for i in range(0,3):
        if S[i] == T[i]:
            result += 1
    print(result)

if __name__ == '__main__':
    main()