def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a==int(a) and a>=10 and a<=99 and (a//10+a%10)>=1
print(main(23))