def gcd_lcm(a, b):
    original_a = a  
    original_b = b  

    while b != 0:
        a, b = b, a % b
    gcd = a
    
    lcm = (original_a * original_b) // gcd 
    
    return gcd, lcm

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
x, y = gcd_lcm(num1, num2)
print(f"GCD: {x}, LCM: {y}")

