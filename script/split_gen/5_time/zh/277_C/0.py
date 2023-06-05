def main():
    n = int(input())
    ab = []
    for _ in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[1])
    print(ab[-1][1]-1)
