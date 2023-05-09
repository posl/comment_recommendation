def main():
    N = int(input())
    S = input()
    queue = []
    for i in range(N):
        if S[i] == '"':
            queue.append(i)
        elif len(queue) % 2 == 0:
            S = S[:i] + '.' + S[i+1:]
    print(S)

if __name__ == '__main__':
    main()