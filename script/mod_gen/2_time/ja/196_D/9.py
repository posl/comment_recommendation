def main():
    H, W, A, B = map(int, input().split())
    print(A*B*2 + (H-A)*(W-B)*2 + (H-A)*(W-B))

if __name__ == '__main__':
    main()