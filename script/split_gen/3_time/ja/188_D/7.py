def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort()
    #print(ABC)
    #print(N, C)
    total = 0
    prev = 0
    for i in range(N):
        #print(ABC[i])
        a, b, c = ABC[i]
        #print(a, b, c)
        if i == 0:
            total += (b - a + 1) * c
            prev = b
        else:
            if prev >= a:
                total += (b - prev) * c
                prev = b
            else:
                total += (b - a + 1) * c
                prev = b
    print(total + C)
