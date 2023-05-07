def main():
    N, A, B = map(int, input().split())
    print((N // A + N // B) - N // lcm(A, B))

if __name__ == '__main__':
    main()