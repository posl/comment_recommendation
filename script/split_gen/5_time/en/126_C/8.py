def main():
    N, K = map(int, input().split())
    if N >= K:
        print(1)
    else:
        print((1/N)*((1/2)**(len(str(bin(K)[2:]))-1)))
