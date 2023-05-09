def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if h_list[i-1] <= h_list[i]:
            count += 1
    print(count)
