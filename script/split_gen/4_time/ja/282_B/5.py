def main():
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            flag = True
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    pass
                else:
                    flag = False
                    break
            if flag:
                count += 1
    print(count)
