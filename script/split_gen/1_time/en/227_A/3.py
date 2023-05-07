def main():
    N, K, A = [int(x) for x in raw_input().split()]
    print (A + K - 1) % N + 1
