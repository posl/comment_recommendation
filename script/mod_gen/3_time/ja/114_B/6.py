def main():
    S = input()
    min = 1000
    for i in range(3, len(S) + 1):
        x = int(S[i - 3:i])
        if abs(x - 753) < min:
            min = abs(x - 753)
    print(min)

if __name__ == '__main__':
    main()