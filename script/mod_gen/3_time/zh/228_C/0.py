def main():
    n, k = map(int, input().split())
    scores = []
    for _ in range(n):
        scores.append(sum(map(int, input().split())))
    print('\n'.join(['Yes' if s < scores[k-1] else 'No' for s in scores]))

if __name__ == '__main__':
    main()