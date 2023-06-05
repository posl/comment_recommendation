def main():
    n = int(input())
    s = list(map(int,input().split()))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                count += 1
    print(count)
