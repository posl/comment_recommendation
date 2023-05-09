def main():
    p = input().split()
    ans = [0]*26
    for i in range(26):
        ans[int(p[i])-1] = chr(i+97)
    print("".join(ans))

if __name__ == '__main__':
    main()