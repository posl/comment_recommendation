def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(min([((A+9)//10)*10,((B+9)//10)*10,((C+9)//10)*10,((D+9)//10)*10,((E+9)//10)*10])+E)
