def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    current_time = T
    current_room = 1
    for i in range(N-1):
        current_time -= A[i]
        if current_time <= 0:
            print("No")
            return
        for x, y in XY:
            if current_room == x:
                current_time = min(T, current_time + y)
        current_room += 1
    print("Yes" if current_time - A[-1] > 0 else "No")
