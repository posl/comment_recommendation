def main():
    N,A,B = map(int,input().split())
    for i in range(N):
        for j in range(N):
            if i < A:
                if j < B:
                    print('.',end='')
                else:
                    print('#',end='')
            else:
                if j < B:
                    print('#',end='')
                else:
                    print('.',end='')
        print()
