def main():
    n = int(input())
    scores = list(map(int, input().split()))
    scores.sort()
    print(scores[-2])

if __name__ == '__main__':
    main()