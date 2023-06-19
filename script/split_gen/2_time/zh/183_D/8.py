def main():
    n, w = map(int, input().split())
    time = [0] * 200005
    for i in range(n):
        s, t, p = map(int, input().split())
        time[s] += p
        time[t] -= p
    for i in range(1, 200005):
        time[i] += time[i - 1]
        if time[i] > w:
            print("No")
            return
    print("Yes")
