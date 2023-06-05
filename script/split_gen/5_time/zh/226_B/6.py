def main():
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split(" "))))
    lst.sort()
    count = 1
    for i in range(1, N):
        if lst[i] != lst[i-1]:
            count += 1
    print(count)
