def printTile(N,A,B):
    for i in range(0,N):
        for j in range(0,A):
            for k in range(0,N):
                for l in range(0,B):
                    if (i+k)%2==0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('', end='')
            print('')
    return
