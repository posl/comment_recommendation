def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    a.sort()
    #print(a)
    for i in range(n-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")
