def main():
    n = int(input())
    s = input()
    arr = [0]
    for i in range(n):
        if s[i] == 'L':
            arr.insert(0,i+1)
        else:
            arr.append(i+1)
    print(*arr)
main()
