def main():
    S = input()
    result = 0
    count = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
        else:
            result = max(result, count)
            count = 0
    result = max(result, count)
    print(result)

if __name__ == '__main__':
    main()