def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A = [str(a) for a in A]
    A = ''.join(A)
    #print(A)
    #pri
