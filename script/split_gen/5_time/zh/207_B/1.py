def main():
    a,b,c,d = map(int,input().split())
    if a > b * c:
        print(-1)
        return
    if b >= d:
        print(1)
        return
    count = 0
    while a <= b * c:
        a = a - c + d
        count += 1
    print(count)
