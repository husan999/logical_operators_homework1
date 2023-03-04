def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a==int(a) and a>=10000 and a<=99999 and (a//10000 < a//1000%10 < a//100%10 < a//10%10 < a%10)
print(main(13589))