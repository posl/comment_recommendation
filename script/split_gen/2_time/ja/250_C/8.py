def main():
    n, q = map(int, input().split())
    # 1-indexed
    balls = [i for i in range(1, n+1)]
    for _ in range(q):
        x = int(input())
        # x-1番目のボールを右隣のボールと入れ替える
        # x-1番目のボールが右端にある場合は左隣のボールと入れ替える
        if x == n:
            balls[x-1], balls[x-2] = balls[x-2], balls[x-1]
        else:
            balls[x-1], balls[x] = balls[x], balls[x-1]
    print(*balls)
