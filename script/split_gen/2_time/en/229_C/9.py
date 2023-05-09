def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        cheese.append(list(map(int, input().split())))
    cheese.sort(key=lambda x: x[0])
    cheese.reverse()
    total = 0
    for c in cheese:
        if W <= 0:
            break
        for _ in range(c[1]):
            if W <= 0:
                break
            total += c[0]
            W -= 1
    print(total)
