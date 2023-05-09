def dodecagon_area():
    r = int(input("Enter radius of circle:"))
    area = 3 * r * r
    print("Area of dodecagon is:", area)
dodecagon_area()
Output:
Enter radius of circle: 4Area of dodecagon is: 48
Enter radius of circle: 15Area of dodecagon is: 675
Enter radius of circle: 80Area of dodecagon is: 19200
In this article, we will see how to find the area of a regular icosagon inscribed in a circle of radius r.
Problem Statement
It is known that the area of a regular icosagon inscribed in a circle of radius a is 5a^2.
Given an integer r, find the area of a regular icosagon inscribed in a circle of radius r.
Constraints
1 ≦ r ≦ 100
r is an integer.
Input
Input is given from Standard Input in the following format:
r
Output
Print an integer representing the area of the regular icosagon.
Sample Input 1
4
Sample Output 1
100
The area of the regular icosagon is 5 × 4^2 = 100.
Sample Input 2
15
Sample Output 2
1575
Sample Input 3
80
Sample Output 3
40000
Solution
