def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += ab[i][0]
        if time > ab[i][1]:
            print("No")
            break
    else:
        print("Yes")
