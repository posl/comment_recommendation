def get_input():
    #Get input from standard input and return a list of lists of integers
    #First line is N and K
    #Second line is a list of N integers
    input = sys.stdin.read().splitlines()
    N, K = [int(i) for i in input[0].split()]
    A = [int(i) for i in input[1].split()]
    return N, K, A
