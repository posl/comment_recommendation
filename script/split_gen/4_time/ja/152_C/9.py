def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    count = 0
    min = n+1
    for i in range(n):
        if p_list[i] < min:
            count += 1
            min = p_list[i]
    print(count)
