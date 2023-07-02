def main(a):
    """
    If the number is positive, increase it to 1,otherwise leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    if  a>0:
         result=a+1

    
    if  a<=0:
         result=a
         
    return result
print(main(-1))    

