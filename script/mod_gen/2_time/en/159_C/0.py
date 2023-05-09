def main():
    L = int(input())
    ans = 0
    for i in range(1, L):
        for j in range(i, L):
            k = L - i - j
            if k < j:
                break
            ans = max(ans, i*j*k)
    print(ans)

if __name__ == '__main__':
    main()