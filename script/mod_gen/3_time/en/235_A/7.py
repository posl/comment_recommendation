def solve():
    abc = int(input())
    a = abc // 100
    b = abc % 100 // 10
    c = abc % 10
    print(a+b+c+(b+c)*10+(c+a)*100)
    return
solve()

if __name__ == '__main__':
    solve()