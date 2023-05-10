def print_pattern(a,b):
    for i in range(a):
        for j in range(b):
            if i%2==0:
                if j%2==0:
                    print('.',end='')
                else:
                    print('#',end='')
            else:
                if j%2==0:
                    print('#',end='')
                else:
                    print('.',end='')
        print('')
n,a,b=map(int,input().split())
for i in range(n):
    print_pattern(a,b)

if __name__ == '__main__':
    print_pattern()