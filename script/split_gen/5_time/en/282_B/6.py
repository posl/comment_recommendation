def main():
    n,m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if s[i].count('o') + s[j].count('o') == m:
                count += 1
    print(count)
main()
