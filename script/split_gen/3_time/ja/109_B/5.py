def main():
    N = int(input())
    W = [input() for _ in range(N)]
    if len(set(W)) != N or not all(W[i][-1] == W[i+1][0] for i in range(N-1)):
        print("No")
    else:
        print("Yes")
