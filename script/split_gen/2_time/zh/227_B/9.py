def main():
    num = int(input())
    guess = list(map(int, input().split()))
    area = []
    for i in range(1, 1000):
        for j in range(1, 1000):
            area.append(4*i*j+3*i+3*j)
    for i in range(num):
        if guess[i] not in area:
            print(i+1)
            break
