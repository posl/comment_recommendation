def main():
    N, X = map(int, input().split())
    #N, X = 4, 12
    #a = [[1, 8], [5, 7], [3, 4], [2, 6]]
    a = []
    for i in range(N):
        a.append(list(map(int, input().split())))
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[0][0] + a[0][1])
    #print(a[1][0] + a[1][1])
    #print(a[2][0] + a[2][1])
    #print(a[3][0] + a[3][1])
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0])
    #print(a[0][1] + a[1][1] + a[2][1] + a[3][1])
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[0][1] + a[1][1] + a[2][1] + a[3][1])
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[0][1] + a[1][1] + a[2][1] + a[3][1] + X)
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[0][1] + a[1][1] + a[2][1] + a[3][1] + X == 12)
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[0][1] + a[
