def main():
    # Step #1. Read input
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Step #2. Solve the problem
    # Step #2.1. Initialize the variable
    total = 0
    
    # Step #2.2. Calculate the total price
    for i in range(N):
        if i % 2 == 0:
            total += A[i]
        else:
            total += A[i] - 1
    
    # Step #2.3. Output the result
    if total <= X:
        print('Yes')
    else:
        print('No')
main()
Problem Statement
Takahashi's shop sells N products. The usual price of the i-th product is A_i yen (Japanese currency). It has a bargain sale today, with a discount of 1 yen off the usual prices for the 2-nd, 4-th, and the subsequent even-indexed products. The 1-st, 3-rd, and the subsequent odd-indexed products are sold for their usual prices. You have X yen. Can you buy all the N products with this money?
Constraints
1 ≦ N ≦ 100
1 ≦ X ≦ 10000
1 ≦ A_i ≦ 100
All values in input are integers.
Input
Input is given from Standard Input in the following format:
N X
A_1 A_2 ... A_N
Output
If you can buy all the N products, print Yes; otherwise, print No.
Sample Input 1
2 3
1 3
Sample Output 1
Yes
You can buy the 1-st product for 1 yen and the 2-nd product for 2 yen, 1 yen off the usual price. You have just enough money, 3 yen, to buy both of them.
Sample Input 2
4 10
3 3 4 4
Sample Output 2
No
You can buy these four products for 3 yen, 2 yen, 4 yen, and 3 yen, respectively. You need 12 yen to buy all of them, and since you have only 10 yen, you cannot buy all of them.
Sample Input 3
8 30
3 1 4 1 5 9 2

if __name__ == '__main__':
    main()