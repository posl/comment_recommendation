def main():
    n = int(input())
    snuke = list(map(int, input().split()))
    takahashi = list(map(int, input().split()))
    snuke_time = [0] * n
    snuke_time[0] = takahashi[0]
    for i in range(1, n):
        snuke_time[i] = max(snuke_time[i - 1] + snuke[i - 1], takahashi[i])
    for i in range(n):
        print(snuke_time[i])
