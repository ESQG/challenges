# -*- coding: UTF-8 -*-
'''I was given a challenge problem by Google:
'Write a function answer(n) that takes an integer n between 3 and 200 inclusive
and computes the number of uneven staircases with n bricks and at least 2 levels.'
That is, it computes the number of strictly decreasing partitions of n; or,
the number of sets (with at least 2 elements) of distinct positive numbers that add up to n.
I struggled to make my code fast enough to meet the challenge,
which is why it contains a map function rather than a for loop.  The function
steps(n, k) calculates the number of strictly decreasing partitions of n with exactly k levels.
(Meaning, how many sets of k distinct positive numbers add up to n.)
It is necessarily recursive; however, for k >= 3 all calculated values of steps(n, k)
are added to a dictionary, and the function always checks the dictionary before recalculating.
This dictionary speeded up the code immensely.

Another way of writing steps(n, k) would be to subtract the triangular number
k*(k+1)/2 from n, then calculate the partitions of the remainder with up to k levels;
stacking a partition of length <= k on top of a staircase (k, k-1, ... 1) ensures uneven steps.
However I found that method to be much slower, even when using the fastest algorithm
for calculating partitions that I could find.

For my own file I have moved the "steps" function outside of the "answer" function, added a "main" function,
and added a while loop at the end to deal with n larger than 200,
specifically n >= 210 as 210 is the next triangular number greater than 200.
'''

known_values = {}
def steps(n, k):
    global known_values #make known_values global so as to remember computed values between calls
    if n <= 0 or k <= 0 or k*(k+1)> 2*n:
        return 0
    elif k == 1 or k*(k+1) == 2*n or k*(k+1) == 2*n-2:
        return 1
    elif k == 2:
        return (n-1) >> 1
    elif (n, k) in known_values:
#can remember previous uses!
        return known_values[(n, k)]
    else:
        total = 0
        total += sum(map(lambda x: steps(n-x*k, k-1), range(1, n/k)))
        #We don't need to round up n/k for k >= 3 because n >= k(k-1)/2 + j*k, to make steps uneven.
        known_values[(n, k)] = total
        return total


def answer(n):
    n = int(n)
    global known_values #quicker if answer has already been called on another n
    total = 0
    if n >= 3:
        total += n-1 >> 1
    if n >= 6:
        total += steps(n, 3)
    if n >=10:
        total += steps(n, 4)
    if n >= 15:
        total += steps(n, 5)
    if n >= 21:
        total += steps(n, 6)
    if n >= 28:
        total += steps(n, 7)
    if n >= 36:
        total += steps(n, 8)
    if n >= 45:
        total += steps(n, 9)
    if n >= 55:
        total += steps(n, 10)
    if n >= 66:
        total += steps(n, 11)
    if n >= 78:
        total += steps(n, 12)
    if n >= 91:
        total += steps(n, 13)
    if n >= 105:
        total += steps(n, 14)
    if n >= 120:
        total += steps(n, 15)
    if n >= 136:
        total += steps(n, 16)
    if n >= 153:
        total += steps(n, 17)
    if n >= 161:
        total += steps(n, 18)
    if n >= 190:
        total += steps(n, 19)
    if n >= 210: #deals with cases not in the original challenge
        k = 20
        while n >= ((k**2+k) >> 1):
            total += steps(n, k)
            k +=1
    return total

def main():
    print("Enter n > 0.  Warning: if n is much bigger than 1000 this may take a while.")
    import sys
    n = int(sys.stdin.readline())
    print(answer(n))

if __name__ == "__main__":
    main()
