def main():
    #Get the year
    year = int(input())
    #Find the next year that the remainder when divided by 4 is 2
    while (year % 4 != 2):
        year += 1
    #Print the year
    print(year)
