def main():
    h,w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if a[j][i] == '#':
                count += 1
        print(count, end=' ')
    print()
