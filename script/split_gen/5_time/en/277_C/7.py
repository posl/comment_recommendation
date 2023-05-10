def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[1])
    #print(ladders)
    current_floor = 1
    for ladder in ladders:
        if ladder[0] >= current_floor:
            current_floor = ladder[1]
        elif ladder[1] >= current_floor:
            current_floor = ladder[1]
    print(current_floor)
