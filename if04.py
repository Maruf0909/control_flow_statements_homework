def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    count = 0
    if a>0:
        count+=1
    if b>0:
        count+=1
    if c>0:
        count+=1
    return count
print(main(-2,7,6))
    
        

        
