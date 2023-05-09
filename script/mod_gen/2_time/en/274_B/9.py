def main():
    # Get input here
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    
    # Calculate result here
    x = [0] * w
    for i in range(w):
        for j in range(h):
            if c[j][i] == '#':
                x[i] += 1
    
    # Print output here
    print(*x)
    
main()

if __name__ == '__main__':
    main()