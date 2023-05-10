def solve():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n):
        for j in range(i+1, n):
            if words[i] == words[j]:
                print("No")
                return
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    solve()