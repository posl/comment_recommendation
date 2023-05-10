def main():
    h, w = map(int, input().split())
    h2, w2 = map(int, input().split())
    print(h*w - (h2*w + h*w2 - h2*w2))

if __name__ == '__main__':
    main()