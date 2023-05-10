def main():
    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append([A, B])
    ladders.sort(key=lambda x:x[1])
    current = -1
    count = 0
    for ladder in ladders:
        if current < ladder[0]:
            current = ladder[1]
            count += 1
    print(count)
