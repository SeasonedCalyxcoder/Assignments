from collections import deque

def is_palindrome(s):
    stack = []
    queue = deque()

    for char in s:
        if char.isalnum():  # Check if the character is alphanumeric
            lower_char = char.lower()  # Convert to lowercase
            stack.append(lower_char)
            queue.append(lower_char)

    while stack:
        if stack.pop() != queue.popleft():
            return False

    return True

user_input = input("Enter a word to check if it's a palindrome: ")

if is_palindrome(user_input):
    print(f"The word, {user_input}, is a palindrome.")
else:
    print(f"The word, {user_input}, is not a palindrome.")