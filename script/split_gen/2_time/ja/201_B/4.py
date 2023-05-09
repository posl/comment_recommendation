def main():
    N = int(input())
    mountain = []
    for i in range(N):
        S, T = input().split()
        mountain.append((S, int(T)))
    mountain.sort(key=lambda x: x[1])
    print(mountain[-2][0])
