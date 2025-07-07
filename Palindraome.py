def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  # Normalize: remove non-alphanumeric, lowercase
    return s == s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("Palindrome!")
    else:
        print("Not a palindrome.")
