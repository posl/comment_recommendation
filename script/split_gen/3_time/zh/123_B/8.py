def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(10*((a-1)//10+(b-1)//10+(c-1)//10+(d-1)//10+(e-1)//10)+max(a%10,b%10,c%10,d%10,e%10))
