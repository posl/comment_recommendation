def main():
    s = input()
    k = int(input())
    s = s.replace(".","")
    if len(s) == 0:
        print(0)
        return
    if k == 0:
        print(len(s))
        return
    ans = 0
    for i in range(len(s)-k):
        ans = max(ans,len(s[i:i+k+1]))
    print(ans)

if __name__ == '__main__':
    main()