def main():
    n,k = map(int, input().split())
    students = []
    for i in range(n):
        students.append(sum(map(int, input().split())))
    students.sort(reverse=True)
    print('Yes' if students[k-1] == students[k] else 'No')

if __name__ == '__main__':
    main()