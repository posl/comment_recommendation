def main():
    h, w = map(int, input().split())
    count = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                count += 1
    print(count)
