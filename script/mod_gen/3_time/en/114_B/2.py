def main():
    S = input()
    min = 999
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        if abs(X-753)<min:
            min = abs(X-753)
    print(min)
main()

if __name__ == '__main__':
    main()