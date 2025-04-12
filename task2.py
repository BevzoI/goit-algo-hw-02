from collections import deque

def define_palindrome():
    d = deque()
    user_input = input("Print your text here -> ").lower().replace(" ", "")
    
    for char in user_input:
        if char.isalnum():
            d.append(char)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return "It's not a palindrome."
    return "It's a palindrome."

result = define_palindrome()
print(result)