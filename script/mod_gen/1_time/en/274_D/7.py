def solve():
    N, x, y = map(int, input().split())
    A = map(int, input().split())
    A = list(A)
    A.append(0)
    A.append(0)
    if x < max(A) or y < max(A):
        return "No"
    else:
        return "Yes"
print(solve())
