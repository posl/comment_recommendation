def main():
    N,A,B = map(int, input().split())
    for i in range(A*N):
        for j in range(B*N):
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
