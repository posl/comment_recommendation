def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if all(c in 'ATGC' for c in s[i:j+1]):
                ans = max(ans, j-i+1)
    print(ans)
main()

if __name__ == '__main__':
    main()