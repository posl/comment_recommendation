def main():
    print("Welcome to the right triangle area calculator!")
    print("Please enter the lengths of the three sides of the triangle, one at a time.")
    ab = int(input("Please enter the length of side AB: "))
    bc = int(input("Please enter the length of side BC: "))
    ca = int(input("Please enter the length of side CA: "))
    print("The area of the triangle is: " + str((ab * bc) / 2))
