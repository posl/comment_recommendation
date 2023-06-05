def problems250_b(n, a, b):
    #print(n, a, b)
    for i in range(a*n):
        for j in range(b*n):
            if (i//a + j//b) % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()
