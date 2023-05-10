def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(2**(n-1)):
        if a[ans] < a[2*i] and a[2*i] < a[2*i+1]:
            ans = 2*i
        elif a[ans] < a[2*i+1] and a[2*i+1] < a[2*i]:
            ans = 2*i+1
    print(ans+1)
