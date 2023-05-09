def main():
    A, B, C, D = map(int, input().split())
    
    if C * D <= B:
        print(-1)
        return
    
    print((A + B * (C * D - B) - 1) // (C * D - B))
main()

if __name__ == '__main__':
    main()