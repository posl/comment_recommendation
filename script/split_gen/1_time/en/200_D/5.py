def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [int(x) for x in input().split()]
    #A = [int(x) for x in sys.stdin.readline().split()]
    #A = [int(x) for x in sys.stdin.readlines()[1].split()]
    #print(N)
    #print(A)
    A = [x % 200 for x in A]
    #pr
