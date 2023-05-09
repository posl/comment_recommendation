def main():
    N = int(input())
    print((N-1)*(1+sum([1/i for i in range(2,N+1)])))
