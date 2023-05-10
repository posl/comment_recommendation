def main():
    s = input()
    t = input()
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()