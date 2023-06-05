def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(n) for n in input().split()]
        result = 0
        for a in A:
            if a % 2 == 1:
                result += 1
        print(result)
