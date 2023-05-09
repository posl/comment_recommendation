def main():
    A,B = [int(i) for i in input().split()]
    print(A+B-max(A,B)+min(A,B))
