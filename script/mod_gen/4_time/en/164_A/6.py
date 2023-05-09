def main():
    s,w = map(int, input().split())
    if w>=s:
        print("unsafe")
    else:
        print("safe")
main()

if __name__ == '__main__':
    main()