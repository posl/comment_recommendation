def main():
    S = input()
    min_diff = 1000
    for i in range(len(S)-2):
        num = int(S[i:i+3])
        if abs(num-753) < min_diff:
            min_diff = abs(num-753)
    print(min_diff)

if __name__ == '__main__':
    main()