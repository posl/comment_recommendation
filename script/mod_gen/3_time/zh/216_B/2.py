def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input())
    if len(set(name_list)) < N:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()