def main():
    n = int(input())
    v_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    x_y_list = [v_list[i] - c_list[i] for i in range(n)]
    x_y_list.sort(reverse=True)
    print(sum([x_y_list[i] for i in range(n) if x_y_list[i] > 0]))
