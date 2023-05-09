def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input())
    if len(names) != len(set(names)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()