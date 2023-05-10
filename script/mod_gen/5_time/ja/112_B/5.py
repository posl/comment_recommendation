def main():
    n, t = map(int, input().split())
    cost_time = []
    for i in range(n):
        cost, time = map(int, input().split())
        cost_time.append((cost, time))
    cost_time.sort(key=lambda x: x[1])
    for cost, time in cost_time:
        if time <= t:
            print(cost)
            return
    print("TLE")

if __name__ == '__main__':
    main()