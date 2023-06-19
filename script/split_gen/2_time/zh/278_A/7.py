def get_input():
    input = raw_input()
    input = input.split(' ')
    N = int(input[0])
    K = int(input[1])
    input = raw_input()
    input = input.split(' ')
    A = [int(i) for i in input]
    return N, K, A
