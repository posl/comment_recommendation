def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    #print(a)
    #print(total)
    for i in range(m):
        #print(i)
        #print(a[i])
        #print(total/4/m)
        if a[i] < total/4/m:
            print("No")
            exit()
    print("Yes")
