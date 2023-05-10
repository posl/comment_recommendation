def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] != t:
            count += 1
    print(count)

if __name__ == '__main__':
    main()