def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        flag = True
        for j in range(i):
            if H[j] >= H[i]:
                flag = False
                break
        if flag:
            count += 1
    print(count)
