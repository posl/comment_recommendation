def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    list = [0, 0, 0, 0]
    for i in range(N):
        list[0] += 1
        for j in range(4):
            if list[j] >= A[i]:
                list[j] -= A[i]
                list[j+1] += 1
            else:
                P += list[j]
                list[j] = 0
    print(P)
