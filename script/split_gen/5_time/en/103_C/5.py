def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    for i in range(N):
        a[i] = a[i] % a[0]
    #print(a)
    print(sum(a))
