def main():
    N = int(input())
    l_list = []
    for i in range(N):
        l_list.append(list(map(int, input().split())))
    l_list.sort()
    count = 1
    for i in range(N-1):
        if l_list[i] != l_list[i+1]:
            count += 1
    print(count)
