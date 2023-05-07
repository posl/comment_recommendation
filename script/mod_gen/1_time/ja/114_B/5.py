def main():
    S = input()
    num = 753
    ans = 1000
    for i in range(len(S)-2):
        ans = min(ans, abs(num - int(S[i:i+3])))
    print(ans)

if __name__ == '__main__':
    main()