def main():
    S = input()
    X = 0
    for i in range(0,len(S)-2):
        X = int(S[i:i+3])
        if abs(X-753) < abs(X-753-1):
            print(abs(X-753))
            break

if __name__ == '__main__':
    main()