def main():
    import math
    N, K = map(int, input().split())
    print(math.ceil(math.log(N, K)))
