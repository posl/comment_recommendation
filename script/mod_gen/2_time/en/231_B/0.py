def main():
    N = int(input())
    candidates = []
    for i in range(N):
        candidates.append(input())
    print(max(set(candidates), key=candidates.count))

if __name__ == '__main__':
    main()