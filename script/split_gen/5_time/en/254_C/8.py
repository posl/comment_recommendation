def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n,k,a)
    for i in range(n-k):
        #print(i, a[i], a[i+k])
        if a[i] > a[i+k]:
            print("No")
            return
    print("Yes")
