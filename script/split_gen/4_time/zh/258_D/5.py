def main():
    n,x = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    # def f(a,b,x):
    #     return a*x+b
    #
    # def f2(ab,x):
    #     return [f(a,b,x) for a,b in ab]
    #
    # def f3(ab,x):
    #     return sum(f2(ab,x))
    #
    # def f4(ab,x):
    #     return sum(f2(ab,x))/x
    #
    # def f5(ab,x):
    #     return sum(f2(ab,x))//x
    #
    # #print(f2(ab,x))
    # print(f3(ab,x))
    # print(f4(ab,x))
    # print(f5(ab,x))
    def f6(ab,x):
        return sum([a*x+b for a,b in ab])
    def f7(ab,x):
        return sum([a*x+b for a,b in ab])/x
    def f8(ab,x):
        return sum([a*x+b for a,b in ab])//x
    #print(f2(ab,x))
    print(f6(ab,x))
    print(f7(ab,x))
    print(f8(ab,x))
