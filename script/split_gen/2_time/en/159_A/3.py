def main():
    #input
    N, M = map(int, input().split())
    #output
    print(N*(N-1)//2 + M*(M-1)//2)
    return
