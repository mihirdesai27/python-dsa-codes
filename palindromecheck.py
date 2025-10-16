def pal(s):
    if s == s[::-1]:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')

s = input("Enter a string: ")
result = pal(s)