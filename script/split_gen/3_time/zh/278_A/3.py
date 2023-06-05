def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        tmp = A.pop(0)
        A.append(tmp)
    print(" ".join(map(str, A)))
