def main():
    N, A, B = map(int, input().split())
    print(sum([i for i in range(1,N+1) if i%A != 0 and i%B != 0]))
