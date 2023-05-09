def odd_numbers():
    '''
    Returns the number of odd numbers in a list of integers
    '''
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        print(len([x for x in A if x % 2 != 0]))
