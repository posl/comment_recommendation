def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    P = [i-1 for i in P]
    Q = [i-1 for i in Q]
    def fact(n):
        return 1 if n == 0 else n*fact(n-1)
    def find_index(permutation):
        index = 0
        for i in range(len(permutation)):
            index += permutation[i]*fact(len(permutation)-i-1)
            for j in range(i+1, len(permutation)):
                if permutation[i] > permutation[j]:
                    permutation[j] -= 1
        return index
    print(abs(find_index(P) - find_index(Q)))
