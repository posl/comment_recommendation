def   main ( N ): 
    #N = int(input())
    max = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            max = i
    print(N // max + max - 2)
