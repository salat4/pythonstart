word = input("Input your word:")


def isPalindrome(s):
    return s == s[::-1]


ans = isPalindrome(word)
if ans:
    print("Yes")
else:
    print("No")
