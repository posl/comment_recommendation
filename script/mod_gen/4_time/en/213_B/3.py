def main():
    n = int(input())
    scores = list(map(int, input().split()))
    sorted_scores = sorted(scores)
    print(scores.index(sorted_scores[-2])+1)

if __name__ == '__main__':
    main()