def main():
    s = input()
    t = input()
    print(min([len(s) - i for i in range(len(t)) if s[i:i+len(t)] == t]))

if __name__ == '__main__':
    main()