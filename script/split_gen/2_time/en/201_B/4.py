def main():
    n = int(input())
    mountain_list = []
    for i in range(n):
        mountain_list.append(input().split())
    mountain_list.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain_list[1][0])
