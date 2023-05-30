def main():
    k,x = map(int,input().split())
    s = x - k + 1
    e = x + k - 1
    for i in range(s,e+1):
        print(i,end=" ")
    print()
main()
