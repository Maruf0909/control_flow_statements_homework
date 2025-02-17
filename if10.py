def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    s=""
    if temp<0:
        s="Freezing"
    if temp>=1 and temp<=10:
        s="Very Cold"
    if temp>10 and temp<21:
        s="Cold"
    if temp>20 and temp<31:
        s="Normal"
    if temp>30 and temp<41:
        s="Hot"
    if temp>40:
        s="Very Hot"
    return s
print(main(-4))