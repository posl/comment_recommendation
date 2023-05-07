def main():
    n, m = map(int, input().split())
    like = [0] * m
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(tmp[0]):
            like[tmp[j+1]-1] += 1
    print(like.count(n))
