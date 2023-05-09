def main():
    # Get the input
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    ps = set(map(int, input().split()))
    
    # Find the nearest integer
    for i in range(0, 100):
        if x - i not in ps:
            print(x - i)
            return
        if x + i not in ps:
            print(x + i)
            return

if __name__ == '__main__':
    main()