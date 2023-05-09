def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    result = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                result = max(result, a[i] + a[j])
            else:
                break
    print(result)
