def main():
    n = int(input())
    ladders = []
    for i in range(n):
        a,b = map(int, input().split())
        ladders.append((min(a,b), max(a,b)))
    ladders.sort(key=lambda x: x[0])
    highest = 0
    for ladder in ladders:
        if ladder[0] > highest:
            break
        else:
            highest = max(highest, ladder[1])
    print(highest)

if __name__ == '__main__':
    main()