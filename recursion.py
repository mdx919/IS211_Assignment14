def fibonnaci(n):
    # i am assuming we are starting with 0 and 1 and n start from 1
    if n < 1:
        return 'incorrect input, enter 1 or more'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


print(fibonnaci(4))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(60, 48))


# Not clear about this function, how can we compare string without some kind of index
# i also do not understand s1 < s2. does it mean that s1[index] less than s2[index] alphabetically
# i will assume, we need an index to compare char
# i will also assume that s1 < s2 means alphabetically or numerically
# i also assume the length of the both s1 and s2 is same
def compareTo(s1, s2, index=0):
    if s1[index] > s2[index]:
        return 1
    elif s1[index] < s2[index]:
        return -1
    else:
        if index + 2 > len(s1) or index + 2 > len(s2):
            return 0
        else:
            return compareTo(s1, s2, index + 1)


print(compareTo('adc', 'adc'))
