#Problem7
def digit_sum(n):
    total=0
    while n>0:
      digit=n%10
      total=total+digit
      n=n//10
    return total

def reverse_num(n):
    reverse_num=0
    while n>0:
       digit=n%10
       reverse_num= reverse_num*10+digit
       n=n//10
    return reverse_num

def is_palindrome(n):
   return n == reverse_num(n)
for n in [2026,12321,9875]:
   print("Number:",n)
   print("Digit sum:",digit_sum(n))
   print("Reverse:",reverse_num(n))
   print("Palindrome:",is_palindrome(n))    
palindromes=[]
for n in range(10,1000):
     if is_palindrome(n):
      palindromes.append(n)
print("Palindromes from 10 to 1000: "+str(len(palindromes)))      



     