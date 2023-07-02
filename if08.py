def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s=""
    #d1=a%10
    #a=a//10
    #d2=a%10
    #a=a//10
    #d3=a%10
    #a=a//10
    if a>9 and a<100:
        if a%2==1:
            s="two-digit odd number"
    if a>9 and a<100:
        if a%2==0:
            s="two-digit even number"
                     
    if a>99 and a<1000:
        if a%2==1:
            s="three-digit odd number"
    if a<-99 and a>-1000:
        if a%2==0:
            s="three-digit even number"
    return s
print(main(-242))