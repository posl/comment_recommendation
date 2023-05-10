def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_height = 0
    total_height = 0
    for i in range(n):
        if(a[i] > max_height):
            max_height = a[i]
        total_height += max_height - a[i]
    print(total_height)
