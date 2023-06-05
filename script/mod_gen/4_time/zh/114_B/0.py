def main():
    S = input()
    S = [int(i) for i in S]
    min_diff = 1000
    for i in range(len(S)-2):
        num = S[i]*100 + S[i+1]*10 + S[i+2]
        min_diff = min(min_diff, abs(num - 753))
    print(min_diff)

if __name__ == '__main__':
    main()