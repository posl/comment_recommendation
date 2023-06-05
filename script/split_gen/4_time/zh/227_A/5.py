def main():
    #n,k,a = map(int, input().split())
    n,k,a = 3, 14, 2
    #n,k,a = 1, 100, 1
    #n,k,a = map(int, input().split())
    #print(n,k,a)
    nlist = [0]*n
    #print(nlist)
    for i in range(k):
        #print(i)
        nlist[a-1] += 1
        #print(nlist)
        a += 1
        if a > n:
            a = 1
    #print(nlist)
    for i in range(n):
        if nlist[i] == max(nlist):
            print(i+1)
            break
main()
