def main():
    N, C = map(int, input().split(' '))
    ABC = []
    for i in range(N):
        ABC.append(list(map(int, input().split(' '))))
    ABC.sort(key=lambda x:x[0])
    ans = 0
    for i in range(N):
        ans += ABC[i][2] * (ABC[i][1] - ABC[i][0] + 1)
    print(ans)
