def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    x_diff = [x_list[i+1] - x_list[i] for i in range(n)]
    x_diff.sort()
    if len(x_diff) == 1:
        print(x_diff[0])
    else:
        x_diff.remove(max(x_diff))
        print(max(x_diff))
