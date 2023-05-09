def main():
    A, B, W = map(int, input().split())
    min_num = 0
    max_num = 0
    for i in range(1, 1001):
        if A * i <= W * 1000 <= B * i:
            min_num = i
            break
    for j in range(1000, 0, -1):
        if A * j <= W * 1000 <= B * j:
            max_num = j
            break
    if min_num == 0 and max_num == 0:
        print("UNSATISFIABLE")
    else:
        print(min_num, max_num)
