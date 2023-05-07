def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]
    def calc_num(l):
        n = 0
        for i in range(len(l)):
            n += l[i] * (math.factorial(len(l) - i - 1))
        return n
    print(abs(calc_num(P) - calc_num(Q)))
