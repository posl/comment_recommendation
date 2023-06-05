def main():
    n = int(input())
    a, b = map(int, input().split())
    s = input()
    print(n, a, b, s)
    #print(s[0:int(n/2)])
    #print(s[int(n/2):n])
    if s[0:int(n/2)] == s[int(n/2):n]:
        print(a*n+b*n)
    else:
        print(a*n+b*(n+1))

if __name__ == '__main__':
    main()