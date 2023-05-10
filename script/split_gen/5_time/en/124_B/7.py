def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 1
    max_h = h_list[0]
    for i in range(1, n):
        if max_h <= h_list[i]:
            count += 1
            max_h = h_list[i]
    print(count)
    return
