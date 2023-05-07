def main():
    #Get Input
    x, y = map(int, input().split())
    #Calculate the number of 10yen stamps needed
    stamps = y - x
    #Check to see if the stamps are already there
    if stamps <= 0:
        stamps = 0
    #Print the answer
    print(stamps)
