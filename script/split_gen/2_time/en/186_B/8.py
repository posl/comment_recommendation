def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [item for sublist in A for item in sublist]
    A = [x for x in A if x != 0]
    print(sum(A) - len(A) * min(A))
