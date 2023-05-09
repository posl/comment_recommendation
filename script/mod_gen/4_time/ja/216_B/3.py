def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    if len(name) == len(set(name)):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()