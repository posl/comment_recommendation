def main():
    n = int(input())
    s = list(map(int,input().split()))
    result = 0
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                result += 1
    print(result)

if __name__ == '__main__':
    main()