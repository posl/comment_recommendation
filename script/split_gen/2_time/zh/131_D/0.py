def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    time = 0
    for a, b in ab:
        time += a
        if time > b:
            print('No')
            break
    else:
        print('Yes')
