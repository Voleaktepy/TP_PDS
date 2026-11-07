#Problem4

print('part(A)')
print(int("7")+3.5)
print(str(10)*3)
print(bool(""),bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True)+float("2.5"))
print(round(2.5),round(3.5))
print(type(10/2))

# Part B — a safe converter
def safe_int(text):
    """Turn text into an int; return None when it is not a number."""
    text = text.strip()
    if text.lstrip("-").isdigit():         
        return int(text)
    try:
        return int(float(text))            
    except ValueError:
        return None                        


for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))
