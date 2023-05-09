def main():
    N, X = map(int, input().split())
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P / 100
        if X < 0:
            print(i+1)
            return
    print(-1)
main()
I am a Japanese student.
I am studying programming for the first time.
I am studying Python.
I am studying at the University of Tokyo.

if __name__ == '__main__':
    main()