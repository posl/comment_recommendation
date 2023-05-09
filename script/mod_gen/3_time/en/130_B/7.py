def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    locations = [0]
    for i in range(N):
        locations.append(locations[i] + L[i])
    print(sum([1 for i in locations if i <= X]))

if __name__ == '__main__':
    main()