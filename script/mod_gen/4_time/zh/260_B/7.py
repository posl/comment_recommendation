def get_input():
    inputs = input().split()
    N = int(inputs[0])
    X = int(inputs[1])
    Y = int(inputs[2])
    Z = int(inputs[3])
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    return N, X, Y, Z, A, B

if __name__ == '__main__':
    get_input()