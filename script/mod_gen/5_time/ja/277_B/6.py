def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(S)
    #print(len(S))
    #print(len(set(S)))
    #print(set(S))
    if N == len(set(S)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()