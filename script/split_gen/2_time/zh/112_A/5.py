def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    points = sorted(points, key=lambda x: x[0] + x[1])
    ans = []
    for i in range(n):
        if i == 0:
            x = points[i][0]
            y = points[i][1]
            if x < 0:
                ans.append('R')
                ans.append('U')
                ans.append('R')
                ans.append('D')
                ans.append('L')
                ans.append('D')
                ans.append('L')
                ans.append('U')
                ans.append('R')
            elif x == 0:
                ans.append('U')
                ans.append('R')
                ans.append('D')
                ans.append('L')
                ans.append('D')
                ans.append('L')
                ans.append('U')
                ans.append('R')
            else:
                ans.append('U')
                ans.append('L')
                ans.append('D')
                ans.append('R')
                ans.append('D')
                ans.append('R')
                ans.append('U')
                ans.append('L')
                ans.append('D')
        else:
            x = points[i][0] - points[i - 1][0]
            y = points[i][1] - points[i - 1][1]
            if x < 0:
                ans.append('R')
                ans.append('U')
                ans.append('R')
                ans.append('D')
                ans.append('L')
                ans.append('D')
                ans.append('L')
                ans.append('U')
                ans.append('R')
            elif x == 0:
                ans.append('U')
                ans.append('R')
                ans.append('D')
                ans.append('L')
                ans.append('D')
                ans.append('L')
                ans.append('U')
                ans.append('R')
            else:
                ans.append('U')
                ans.append('L')
                ans.append('D')
                ans.append('R')
                ans.append('D')
                ans.append('R')
                ans.append('U')
                ans.append('L')
                ans.append('D')
    print(len(ans))
    print(''.join(ans))
