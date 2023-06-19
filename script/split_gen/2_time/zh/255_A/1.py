def main():
    r,c = map(int,raw_input().split())
    A = []
    for i in range(2):
        A.append(map(int,raw_input().split()))
    print A[r-1][c-1]
