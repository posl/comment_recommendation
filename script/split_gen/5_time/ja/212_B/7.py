def main():
    #input
    x = input()
    #output
    if x[0]==x[1]==x[2]==x[3] or \
        x[1]==str((int(x[0])+1)%10) and x[2]==str((int(x[1])+1)%10) and x[3]==str((int(x[2])+1)%10):
        print("Weak")
    else:
        print("Strong")
