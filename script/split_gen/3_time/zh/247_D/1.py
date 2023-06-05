def main():
    q = int(input())
    arr = []
    for i in range(q):
        arr.append(list(map(int, input().split())))
    for item in arr:
        if item[0] == 1:
            print(item[1] * item[2])
        else:
            print(item[1])
