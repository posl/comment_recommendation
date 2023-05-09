def main():
    S = input()
    K = int(input())
    for i, s in enumerate(S):
        if s == "1":
            continue
        if i + int(s) >= K:
            print(s)
            break
        K -= int(s)

if __name__ == '__main__':
    main()