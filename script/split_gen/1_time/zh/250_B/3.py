def print_tile(a,b):
    for i in range(a):
        if i%2==0:
            print("#"*b,end="")
        else:
            print("."*b,end="")
        print()
    return
