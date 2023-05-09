def main():
    n,m = map(int,input().split())
    requests = [list(map(int,input().split())) for _ in range(m)]
    requests.sort(key=lambda x: x[1])
    removed = 0
    last = 0
    for a,b in requests:
        if a > last:
            removed += 1
            last = b-1
    print(removed)

if __name__ == '__main__':
    main()