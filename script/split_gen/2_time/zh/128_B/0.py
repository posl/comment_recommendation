def main():
    num = int(input())
    rest = []
    for i in range(num):
        name, score = input().split()
        rest.append([name, int(score)])
    rest = sorted(rest, key=lambda x: (x[0], -x[1]))
    for i in range(num):
        print(rest[i][1])
