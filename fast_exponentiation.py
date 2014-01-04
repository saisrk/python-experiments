"""
This is way of computing n ^ p by using effective recursion.
If p = 0 then return 1
If p = even then compute exp(n, p/2) and square the result
If p is odd then compute exp(n, p-1) 
"""
def exponentiate(base, exp):
    """This the main method calculating the exponentiation"""
    if exp == 0:
        return 1
    elif exp % 2 != 0:
        return base * exponentiate(base, exp/2)
    else:
        t = exponentiate(base, exp -1)
        return t * t
    
if __name__ == '__main__':
    n = int(raw_input("Enter the value for Base"))
    p = int(raw_input("Enter the value for Exponent"))
    print exponentiate(n, p)
