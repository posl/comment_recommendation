def get_magic_number(N, A, B, C, l):
    min_magic = 100000000
    for i in range(4 ** N):
        magic = 0
        a = 0
        b = 0
        c = 0
        for j in range(N):
            if i % 4 == 0:
                a += l[j]
                magic += 10
            elif i % 4 == 1:
                b += l[j]
                magic += 10
            elif i % 4 == 2:
                c += l[j]
                magic += 10
            i = i // 4
        if a > 0 and b > 0 and c > 0:
            magic += abs(a - A) + abs(b - B) + abs(c - C)
            if magic < min_magic:
                min_magic = magic
    return min_magic

if __name__ == '__main__':
    get_magic_number()