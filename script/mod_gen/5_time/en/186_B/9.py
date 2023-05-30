def solve(H, W, A):
    min_num = min([min(a) for a in A])
    return sum([sum([a - min_num for a in a]) for a in A])
H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
print(solve(H, W, A))
