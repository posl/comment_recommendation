def main():
    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))
    ladders.sort(key=lambda x: x[1])
    current_floor = 1
    for ladder in ladders:
        if ladder[0] > current_floor:
            current_floor = ladder[0]
        if ladder[1] >= current_floor:
            current_floor = ladder[1]
    print(current_floor)
