def problems250_b(n,a,b):
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+j)%2==0 and (k+l)%2==0:
                        print('.',end='')
                    elif (i+j)%2==0 and (k+l)%2!=0:
                        print('#',end='')
                    elif (i+j)%2!=0 and (k+l)%2==0:
                        print('#',end='')
                    elif (i+j)%2!=0 and (k+l)%2!=0:
                        print('.',end='')
                print('')
        print('')

if __name__ == '__main__':
    problems250_b()