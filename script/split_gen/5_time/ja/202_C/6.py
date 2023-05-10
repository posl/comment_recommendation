def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    c.sort()
    count = 0
    for i in range(n):
        #print(i)
        #print(a[i])
        #print(b[c[i]-1])
        if a[i] == b[c[i]-1]:
            #print("OK")
            count += 1
    print(count)
