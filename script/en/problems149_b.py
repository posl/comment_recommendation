#Problem Statement
#Takahashi has A cookies, and Aoki has B cookies.
#Takahashi will do the following action K times:
#If Takahashi has one or more cookies, eat one of his cookies.
#Otherwise, if Aoki has one or more cookies, eat one of Aoki's cookies.
#If they both have no cookies, do nothing.
#In the end, how many cookies will Takahashi and Aoki have, respectively?
#
#Constraints
#0 ≦ A ≦ 10^{12}
#0 ≦ B ≦ 10^{12}
#0 ≦ K ≦ 10^{12}
#All values in input are integers.
#
#Input
#Input is given from Standard Input in the following format:
#A B K
#
#Output
#Print the numbers of Takahashi's and Aoki's cookies after K actions.
#
#Sample Input 1
#2 3 3
#
#Sample Output 1
#0 2
#Takahashi will do the following:
#He has two cookies, so he eats one of them.
#Now he has one cookie left, and he eats it.
#Now he has no cookies left, but Aoki has three, so Takahashi eats one of them.
#Thus, in the end, Takahashi will have 0 cookies, and Aoki will have 2.
#
#Sample Input 2
#500000000000 500000000000 1000000000000
#
#Sample Output 2
#0 0
#Watch out for overflows.

def 