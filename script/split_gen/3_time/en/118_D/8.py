def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a = [str(i) for i in a]
    #print(a)
    #print(a[0])
    #print(a[0] * (n // len(a[0])))
    #print(a[0] * (n // len(a[0])) + a[0][:n % len(a[0])])
    print(a[0] * (n // len(a[0])) + a[0][:n % len(a[0])])
