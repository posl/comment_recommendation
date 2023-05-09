def main():
    a, b, w = map(int, input().split())
    w *= 1000
    max_num = 0
    min_num = 0
    for i in range(1, w + 1):
        if a * i <= w and w <= b * i:
            if max_num == 0:
                max_num = i
            min_num = i
    if min_num == 0:
        print("UNSATISFIABLE")
    else:
        print(min_num, max_num)
