def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += ab[i][0]
        if t > ab[i][1]:
            print('No')
            exit()
    print('Yes')
