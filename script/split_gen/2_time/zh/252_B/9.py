def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #print(n, k)
    #print(a)
    #print(b)
    for i in range(k):
        a[b[i] - 1] = 0
    #print(a)
    if max(a) == 0:
        print("No")
    else:
        print("Yes")
