def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[1], reverse=True)
    current = 1
    for ladder in ladders:
        if ladder[0] <= current <= ladder[1]:
            current = ladder[1]
        elif ladder[1] <= current <= ladder[0]:
            current = ladder[0]
    print(current)
