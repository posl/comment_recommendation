def main():
    v,t,s,d = map(int, input().split())
    print("Yes" if (t * v <= d <= s * v) else "No")

if __name__ == '__main__':
    main()