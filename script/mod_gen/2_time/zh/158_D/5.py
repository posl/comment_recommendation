def main():
    string = input()
    Q = int(input())
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            string = string[::-1]
        else:
            if query[1] == '1':
                string = query[2] + string
            else:
                string = string + query[2]
    print(string)

if __name__ == '__main__':
    main()