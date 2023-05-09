def main():
    num = int(input())
    height = list(map(int, input().split()))
    max_num = 0
    count = 0
    for i in range(1,num):
        if height[i-1] >= height[i]:
            count += 1
        else:
            count = 0
        if max_num < count:
            max_num = count
    print(max_num)
