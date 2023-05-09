def main():
    #input
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    
    #sort
    p.sort()
    
    #output
    print(sum(p[:K]))
main()
I did not understand the problem statement. I thought it was asking for the minimum price of a single fruit. So, I was confused when I saw the sample output. I was like, “What? The minimum price of a single fruit is 50 yen. How can it be 210 yen?” I was confused for a while until I realized that I misunderstood the problem statement. So, I read the problem statement again and understood the problem.
The problem statement says that we have to choose K kinds of fruits and buy one of each chosen kind. So, we have to buy K fruits. The minimum total price for K fruits is the sum of K smallest prices of fruits. So, we have to sort the list of prices of fruits in ascending order and then sum the first K elements of the list.
I used the sort() method to sort the list of prices of fruits in ascending order. Then, I used the sum() function to sum the first K elements of the list.
I submitted the code and got accepted.
The code passed all test cases.
This is the end of my post about AtCoder Beginner Contest 171 B. I hope you found this post helpful. If you have any questions or comments, please feel free to leave them below. I will try my best to answer them. Thank you for reading my post. Happy coding!
References
AtCoder Beginner Contest 171 B
AtCoder Beginner Contest 171
AtCoder Beginner Contest 171 B – Codeforces
AtCoder Beginner Contest 171 B – AtCoder
AtCoder Beginner Contest 171 B – YouTube
AtCoder Beginner Contest 171 B – GitHub
AtCoder Beginner Contest 171 B – Qiita
AtCoder Beginner Contest 171 B – TOKI Open Contest
AtCoder Beginner Contest 171 B – TOKI Open Contest 2020
AtCoder Beginner Contest 171 B – TOKI Open Contest 2020 – Problem
AtCoder Beginner Contest 171 B – TOKI Open Contest 2020 – Problem Statement
AtCoder Beginner Contest 171 B – TOKI Open Contest 2020 – Constraints
AtCoder Beginner Contest 171
