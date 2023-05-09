def main():
    N = int(input())
    S_list = []
    for i in range(N):
        S_list.append(input())
    if S_list.count("For") > N/2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()