def main():
    W = int(input())
    N = W//2
    A = [2]*N
    if W%2 == 1:
        N += 1
        A.append(1)
    print(N)
    print(*A)
