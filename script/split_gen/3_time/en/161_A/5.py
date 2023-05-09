def main():
    #Get the input from the user
    x, y, z = map(int, input().split())
    #Swap the contents of the boxes A and B
    x, y = y, x
    #Swap the contents of the boxes A and C
    x, z = z, x
    #Print the integers contained in the boxes A, B, and C, in this order, with space in between.
    print(x, y, z)
