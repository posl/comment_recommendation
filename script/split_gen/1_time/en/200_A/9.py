def main():
    # get the year
    year = int(input())
    
    # calculate the century
    century = year // 100
    if year % 100 != 0:
        century += 1
        
    # print the century
    print(century)
