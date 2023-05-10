def main():
    P = list(map(int, input().split()))
    alp = [chr(i) for i in range(97, 97+26)]
    ans = ""
    for i in range(26):
        ans += alp[P[i]-1]
    print(ans)

if __name__ == '__main__':
    main()