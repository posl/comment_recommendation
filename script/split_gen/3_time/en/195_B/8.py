def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_oranges = -1
    max_oranges = -1
    for i in range(1, W+1):
        if A * i <= W <= B * i:
            min_oranges = i
            break
    for i in range(W, 0, -1):
        if A * i <= W <= B * i:
            max_oranges = i
            break
    if min_oranges == -1:
        print("UNSATISFIABLE")
    else:
        print(min_oranges, max_oranges)
