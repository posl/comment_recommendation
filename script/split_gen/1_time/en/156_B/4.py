def main():
    N, K = map(int, input().split())
    print(len(str(N).encode('utf-8').hex())//2)
