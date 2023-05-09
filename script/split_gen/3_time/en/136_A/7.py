def main():
    # Write your code here
    A,B,C = map(int,input().split())
    if C >= A-B:
        print(C-(A-B))
    else:
        print(C)
