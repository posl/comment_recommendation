def main():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    #print(N//(A*B), N//A, N//B)
    print(N - N//A - N//B + N//(A*B))
