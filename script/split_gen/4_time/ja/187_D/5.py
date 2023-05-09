def main():
    N = int(input())
    AB = []
    for _ in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    A_sum = sum([AB[i][0] for i in range(N)])
    B_sum = sum([AB[i][1] for i in range(N)])
    A_cnt = 0
    B_cnt = 0
    for i in range(N):
        A_cnt += AB[i][0]
        B_cnt += AB[i][1]
        if A_cnt > B_sum - B_cnt:
            print(i+1)
            break
