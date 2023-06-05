def main():
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    count=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    count += 1
                    break
    print(count)
