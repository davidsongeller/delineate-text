import textwrap

# Get input from user
long_text = input("Enter a long line of text: ")

# Define maximum width for shorter lines
width = 40

# Wrap long text into shorter lines
wrapped_text = textwrap.fill(long_text, width=width, replace_whitespace=False)

# Print the wrapped text
print(wrapped_text)
