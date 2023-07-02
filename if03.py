def main(a):
    """
    If the number is positive, increase it to 1,if the number is negative decrease it to 2.
    If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    if a>0:
        result = a+1
    if a<=0:
        result = a-2
    if a==0:
        result=10

    return result
print(main(0))