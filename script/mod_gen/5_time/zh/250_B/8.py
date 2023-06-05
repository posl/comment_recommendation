def print_tile(n,a,b):
    for i in range(a):
        for j in range(n):
            for k in range(b):
                if (i+j)%2==0:
                    if k==0:
                        print('.',end='')
                    else:
                        print('#',end='')
                else:
                    if k==0:
                        print('#',end='')
                    else:
                        print('.',end='')
            print('')
        print('')
n,a,b=map(int,input().split())
print_tile(n,a,b)
