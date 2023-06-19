def main():
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2:
        print(1)
    else:
        print((N-1)*(N-2)//2)
