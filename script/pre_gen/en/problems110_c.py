#Problem Statement
#You are given strings S and T consisting of lowercase English letters.
#You can perform the following operation on S any number of times:
#Operation: Choose two distinct lowercase English letters c_1 and c_2, then replace every occurrence of c_1 with c_2, and every occurrence of c_2 with c_1.
#Determine if S and T can be made equal by performing the operation zero or more times.
#
#Constraints
#1 ≦ |S| ≦ 2 × 10^5
#|S| = |T|
#S and T consists of lowercase English letters.
#
#Input
#Input is given from Standard Input in the following format:
#S
#T
#
#Output
#If S and T can be made equal, print Yes; otherwise, print No.
#
#Sample Input 1
#azzel
#apple
#
#Sample Output 1
#Yes
#azzel can be changed to apple, as follows:
#Choose e as c_1 and l as c_2. azzel becomes azzle.
#Choose z as c_1 and p as c_2. azzle becomes apple.
#
#Sample Input 2
#chokudai
#redcoder
#
#Sample Output 2
#No
#No sequences of operation can change chokudai to redcoder.
#
#Sample Input 3
#abcdefghijklmnopqrstuvwxyz
#ibyhqfrekavclxjstdwgpzmonu
#
#Sample Output 3
#Yes

def 