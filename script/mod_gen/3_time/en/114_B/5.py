def main():
    S = input()
    x = 753
    for i in range(len(S)-2):
        x = min(x, abs(int(S[i:i+3])-753))
    print(x)

if __name__ == '__main__':
    main()