def main():
    #input
    c1, c2, c3 = input().split()
    #process
    if c1 == c2 and c2 == c3:
        print('Won')
    else:
        print('Lost')
    #output
