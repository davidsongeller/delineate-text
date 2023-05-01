def format_input(input_string, max_width):
    words = input_string.split()
    output_lines = []
    line = ""
    for word in words:
        if len(line + word) < max_width:
            line += word + " "
        else:
            output_lines.append(line.rstrip())
            line = word + " "
    output_lines.append(line.rstrip())
    final_output = ""
    for line in output_lines:
        if line.endswith(","):
            final_output += line[:-1] + "\n"
        else:
            final_output += line + "\n"
    return final_output

input_string = input("Enter a long line of text: ")
while True:
    max_width_input = input("Enter the maximum width for each line: ")
    if max_width_input.isdigit():
        max_width = int(max_width_input)
        break
    else:
        print("Invalid input. Please enter a valid integer.")

formatted_input = format_input(input_string, max_width)

print(formatted_input)
