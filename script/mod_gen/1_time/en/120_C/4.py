def main():
    S = input()
    N = len(S)
    B = 0
    for s in S:
        if s == '1':
            B += 1
    R = N - B
    ans = min(B, R) * 2
    print(ans)

if __name__ == '__main__':
    main()