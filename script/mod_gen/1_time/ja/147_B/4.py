def main():
    S = input()
    half = len(S) // 2
    count = 0
    for i in range(half):
        if S[i] != S[-(i+1)]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()