def main():
    N = int(input())
    AB = []
    for _ in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
    AB.sort(key=lambda x: x[1])
    time = 0
    for a, b in AB:
        time += a
        if time > b:
            print("No")
            break
    else:
        print("Yes")

if __name__ == '__main__':
    main()