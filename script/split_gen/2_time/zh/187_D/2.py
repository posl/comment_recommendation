def main():
    n = int(input())
    ab = [list(map(int, input().split())) for i in range(n)]
    ab.sort(key=lambda x: 2*x[0]+x[1], reverse=True)
    #print(ab)
    x = 0
    for i in range(n):
        x += ab[i][0]
        if x > sum([ab[j][1] for j in range(i+1)]):
            print(i+1)
            break
    else:
        print(n)
