def main():
    A,B,C = map(int,input().split())
    if A==B and B==C:
        print("否")
    elif A==B or B==C or A==C:
        print("是")
    else:
        print("否")
