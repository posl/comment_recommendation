def main():
    X, Y, N = map(int, input().split())
    if N%3 == 0:
        print(Y*(N/3))
    elif N%3 == 1:
        print(Y*(N//3)+X)
    elif N%3 == 2:
        print(Y*(N//3)+2*X)
    else:
        print('error')
