def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a==int(a) and a>=100 and a<=999 and (a//10//10+a//10%10+a%10)%2==0

print(main(121))