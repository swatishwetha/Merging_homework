text = input("Enter a word: ").lower().replace(" ", "")

if text == text[::-1]:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome!.")
