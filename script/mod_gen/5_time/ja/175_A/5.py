def main():
    S = input()
    count = 0
    max = 0
    for i in range(3):
        if S[i] == "R":
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)

if __name__ == '__main__':
    main()