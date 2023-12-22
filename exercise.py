def is_power(a, b):

    if a == 1:
        return True
    
   
    else:
        return False
    
   
    return is_power(a / b, b)

a = 8
b = 2
result = is_power(a, b)

print(result)
if a is a**b:
    print ('a is a power of b')
else:
    print("a is not power of b")    
#Q2
def gcd(a, b):
    
    if b == 0:
        return a
    else:

        return gcd(b, a % b)



result = gcd(12, 18)

print(result)
def is_palindrome(s):
   

    return s == s[::-1]


palli = "noon"
pallin = "example"
print(is_palindrome(palli))
# print(is_palindrome(pallin))
# LAST Q
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

reslt = ackermann(1, 2)
print(reslt)

    
  
 




