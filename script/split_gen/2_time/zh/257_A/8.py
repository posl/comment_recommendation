def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    data.sort()
    left = data[0][0]
    right = data[0][1]
    for i in range(1, n):
        if data[i][0] <= right:
            if data[i][1] > right:
                right = data[i][1]
        else:
            print(left, right)
            left = data[i][0]
            right = data[i][1]
    print(left, right)
