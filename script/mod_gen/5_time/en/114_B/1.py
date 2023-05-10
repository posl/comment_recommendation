def main():
    S = input()
    N = len(S)
    ans = 753
    for i in range(N-2):
        ans = min(ans, abs(753 - int(S[i:i+3])))
    print(ans)

if __name__ == '__main__':
    main()