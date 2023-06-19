def play_list():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    t %= sum(a)
    for i in range(n):
        t -= a[i]
        if t < 0:
            print(i + 1, -t)
            break

if __name__ == '__main__':
    play_list()