def main():
    line = input()
    S,W = line.split()
    S = int(S)
    W = int(W)
    if S > W:
        print("安全")
    else:
        print("不安全")

if __name__ == '__main__':
    main()