def main():
    n,a,b = map(int,input().strip().split())
    for i in range(0,n):
        for j in range(0,a):
            for k in range(0,n):
                for l in range(0,b):
                    if (i+j)%2==0:
                        print('.',end='')
                    else:
                        print('#',end='')
            print('')
    return
