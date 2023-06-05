def main():
    n,k = map(int, input().split())
    scores = []
    for i in range(n):
        scores.append(list(map(int, input().split())))
    scores.sort(key=lambda x: sum(x), reverse=True)
    scores = scores[:k]
    scores = [sum(x) for x in scores]
    scores.sort(reverse=True)
    for i in range(n):
        if sum(scores[i:]) < scores[k-1]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()