def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    max_dist = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                dist = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
                if dist > max_dist:
                    max_dist = dist
    print(max_dist)

if __name__ == '__main__':
    main()