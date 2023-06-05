def main():
    a,b = map(int, input().split())
    a_str = str(a)
    b_str = str(b)
    if a_str == b_str:
        print(a_str*a)
    elif a_str < b_str:
        print(a_str*b)
    else:
        print(b_str*a)
