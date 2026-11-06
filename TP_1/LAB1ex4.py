#This is part a

print('part(A)')

print(int("7")+3.5)
print(str(10)*3)
print(bool(""),bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True)+float("2.5"))
print(round(2.5),round(3.5))
print(type(10/2))

print("This is part b")


# Question B, write a function safe_int(text) that turns a string into an int. It must accept spaces around the number, negative numbers and decimals ("3.9" → 3), and return None when the text is not a number.
def safe_int(text):
    try:
        return int(float(text.strip()))
    except ValueError:
        return None
print(safe_int("  -3.9  ")) 
print(safe_int("abc"))

# Part B — a safe converter
def safe_int(text):
    """Turn text into an int; return None when it is not a number."""
    text = text.strip()
    if text.lstrip("-").isdigit():         # "42" or "-42"
        return int(text)
    try:
        return int(float(text))            # "3.9" -> 3
    except ValueError:
        return None                        # "abc", "", "12a"


for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))
