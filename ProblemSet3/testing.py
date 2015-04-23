# -*- coding: utf-8 -*-
'''
# PROBLEM 4
def myLog(x, b):

    largest_value = 0
    power = 0

    while largest_value < x:
        power += 1
        if x > 0 and b >= 2:
            if b**power > x:
                power -= 1
                break
            largest_value = b**power
    return power

print myLog(100, 3)
'''
'''
#PROBLEM 5

def laceStrings(s1, s2):
    laced_string = []
    if len(s1) == len(s2):
        for i in range(len(s1)):
            laced_string.append(s1[i])
            for j in range(len(s2[i])):
                laced_string.append(s2[i])

    elif len(s1) > len(s2):
        for i in range(len(s2)):
            laced_string.append(s1[i])
            for j in range(len(s2[i])):
                laced_string.append(s2[i])
        laced_string.append(s1[len(s2)::])

    elif len(s2) > len(s1):
        for i in range(len(s1)):
            laced_string.append(s1[i])
            for j in range(len(s2[i])):
                laced_string.append(s2[i])
        laced_string.append(s2[len(s1)::])
    laced_string = "".join(laced_string)
    return laced_string


s1 = 'abcd'
s2 = 'efghijk'
print laceStrings(s1, s2)
'''
'''
# PROBLEM 6
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], out+s1[0]+s2[0])
    return helpLaceStrings(s1, s2, '')

print laceStringsRecur('uf', 'wvqhdypo')
'''
# n = 15
def McNuggets(n):

    if n % 6 == 0:
        return True
    if (n % 9) % 6 == 0:
        return True
    if ((n % 20) % 9) % 6 == 0:
        return True
    return False

print McNuggets(23)
