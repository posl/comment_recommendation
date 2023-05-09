def main():
    N = int(input())
    list = []
    for i in range(N):
        S, T = input().split()
        list.append(S + T)
    if len(set(list)) == len(list):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()