def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_ans = W // B
    max_ans = W // A
    if min_ans * B <= W <= max_ans * A:
        print(min_ans, max_ans)
    else:
        print("UNSATISFIABLE")
