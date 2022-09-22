def isPalindrome(s):
    s1 = s.replace(' ', '')
    s1 = s1.lower()
    s2 = s1[::-1];
    return True if s1 == s2 else False
   
s = "A man, a plan, a canal: Panama"
if (isPalindrome(s)):
    print ("Sentence is palindrome.")
else:
    print ("Sentence is not palindrome.")
