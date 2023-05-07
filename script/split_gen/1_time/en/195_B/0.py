def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_oranges = W // B
    max_oranges = W // A
    if W % B != 0:
        min_oranges += 1
    if W % A != 0:
        max_oranges -= 1
    if min_oranges > max_oranges:
        print('UNSATISFIABLE')
    else:
        print(min_oranges, max_oranges)
