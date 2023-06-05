def main():
    n = int(input())
    file_name = {}
    for i in range(n):
        s = input()
        if s in file_name:
            file_name[s] += 1
            print(s+'('+str(file_name[s])+')')
        else:
            file_name[s] = 0
            print(s)

if __name__ == '__main__':
    main()