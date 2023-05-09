def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print(sum([1 for i in range(1,31) for j in range(1,31) for k in range(1,31) if h1 == i+j+k and h2 == i+2*j+3*k and h3 == 4*i+5*j+6*k and w1 == i+4*j and w2 == j+5*k and w3 == 2*i+3*j+6*k]))

if __name__ == '__main__':
    main()