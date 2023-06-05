def main():
    h,a = map(int,input().split())
    count = 0
    while h > 0:
        h = h - a
        count += 1
    print(count)
