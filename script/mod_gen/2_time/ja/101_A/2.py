def main():
    S = input()
    result = 0
    for i in range(4):
        if S[i] == '+':
            result += 1
        else:
            result -= 1
    print(result)

if __name__ == '__main__':
    main()