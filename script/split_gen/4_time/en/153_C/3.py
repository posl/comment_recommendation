def main():
    N, K = map(int, input().split())
    H = sorted([int(x) for x in input().split()], reverse=True)
    if K > N:
        print(0)
    else:
        print(sum(H[K:]))
