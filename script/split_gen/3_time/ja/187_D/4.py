def main():
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    A_sum = 0
    B_sum = 0
    for i in range(N):
        A_sum += AB[i][0]
        B_sum += AB[i][1]
        if A_sum < B_sum:
            print(i + 1)
            return
    print(N)
