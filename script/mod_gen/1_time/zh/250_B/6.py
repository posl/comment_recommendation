def main():
    n,a,b = map(int,input().split())
    #n = int(n)
    #a = int(a)
    #b = int(b)
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2 == 0:
                        print('.',end='')
                    else:
                        print('#',end='')
            print()
main()
