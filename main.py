import textwrap

def format_input(input_string, max_width):
    output_lines = textwrap.wrap(input_string, width=max_width, replace_whitespace=False)
    final_output = "\n".join(output_lines)
    return final_output

def get_input():
    while True:
        input_string = input("Enter a long line of text: ")
        if input_string:
            return input_string

def get_max_width():
    while True:
        max_width_input = input("Enter the maximum width for each line: ")
        if max_width_input.isdigit():
            return int(max_width_input)
        else:
            print("Invalid input. Please enter a valid integer.")

def main():
    input_string = get_input()
    max_width = get_max_width()
    formatted_input = format_input(input_string, max_width)
    print(formatted_input)

if __name__ == '__main__':
    main()
