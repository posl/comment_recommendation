def problem201_b():
    n = int(input())
    mountains = []
    for i in range(n):
        name, height = input().split()
        mountains.append((name, int(height)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])
