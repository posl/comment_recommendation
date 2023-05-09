def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_num, max_num = 0, 0
    for i in range(1, W+1):
        if A * i <= W <= B * i:
            min_num = i
            break
    for i in range(W, 0, -1):
        if A * i <= W <= B * i:
            max_num = i
            break
    if min_num == 0:
        print("UNSATISFIABLE")
    else:
        print(min_num, max_num)

if __name__ == '__main__':
    main()