def main():
    S = input()
    K = int(input())
    s = S.replace(".","X")
    s = s.replace("X"*K,"."*K)
    print(len(s))

if __name__ == '__main__':
    main()