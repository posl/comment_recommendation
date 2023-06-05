def main():
    num = int(input())
    height = list(map(int, input().split()))
    max_height = 0
    for i in range(num):
        if height[i] > max_height:
            max_height = height[i]
    print(max_height)
