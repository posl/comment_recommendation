def main():
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
    AB.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += AB[i][0]
        if time > AB[i][1]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()