def get_see_count():
    N = int(input())
    H = list(map(int, input().split()))
    see_count = 0
    for i in range(N):
        see = True
        for j in range(i):
            if H[i] < H[j]:
                see = False
                break
        if see:
            see_count += 1
    print(see_count)

if __name__ == '__main__':
    get_see_count()