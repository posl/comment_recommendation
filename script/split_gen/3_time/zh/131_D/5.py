def main():
    N = int(input())
    list = []
    for i in range(N):
        A, B = map(int, input().split())
        list.append([A, B])
    list.sort(key=lambda x: x[1])
    sum = 0
    for i in range(N):
        sum += list[i][0]
        if sum > list[i][1]:
            print("No")
            break
    else:
        print("Yes")
