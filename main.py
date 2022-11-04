s = input()
# def reverseString(s):
vowel = {'a','e','i','o','u','A','E','I','O','U'}
s = list(s)
left = 0
right = len(s)-1
while left<right:
    if s[left] in vowel and s[right] in vowel:
        s[left],s[right] = s[right],s[left]
        right -=1
        left +=1
    elif s[left] not in vowel:
        left+=1
    else:
        right-=1
    new = ''.join(s)
print(new)
# print(type(new))
# reverseString(s)
# if __name__ == "__main__":
#     s = "hello"
#     reverseString(s)
#     print(s)
