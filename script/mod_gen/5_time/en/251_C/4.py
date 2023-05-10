def main():
    n = int(input())
    max_score = 0
    max_score_index = 0
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if t > max_score:
            max_score = t
            max_score_index = i + 1
    print(max_score_index)

if __name__ == '__main__':
    main()