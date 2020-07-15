import sys
import math
from functools import reduce

def is_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True


# First draft - not awesome!
def sieve(n):
    nums = [x for x in range(2, n + 1)]
    i = 0
    while i < len(nums)/nums[i]:
        nums = [n for n in nums if n == nums[i] or n % nums[i] != 0]
        i = i + 1
    return nums

print(sieve(100))

'''Please disregard comment about the above being the first draft. 
 It has been promoted to only draft.'''
