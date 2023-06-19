def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [a for b in A for a in b]
    print(sum(A) - max(A) * H * W)
main()
