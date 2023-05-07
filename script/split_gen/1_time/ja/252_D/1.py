def main():
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if a[i] == a[j] or a[j] == a[k] or a[k] == a[i]:
                    continue
                elif a[i] + a[j] > a[k] and a[i] + a[k] > a[j] and a[j] + a[k] > a[i]:
                    count += 1
    print(count)
