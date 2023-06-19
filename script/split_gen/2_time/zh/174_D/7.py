def main():
    N = int(input())
    c = input()
    count = 0
    # 先把W移到最左边
    for i in range(N):
        if c[i] == 'W':
            count += 1
    print(count)
