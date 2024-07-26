a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
a = "Hello World!"
print(a[1])
print(len(a))

# Looping Through a String
for x in "banana":
    print(x)
    
# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Check if NOT
print("expensive" not in txt)

# Slicing
b = "Hello World!"
print(b[2:7])
print(b[:7])
print(b[2:])
print(b[-7:-2])

# Modify Strings
a = "  Hello World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.strip().split(" "))

# Format Strings
txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)