## Inputs

- A long line of text
- The maximum width for each line

### Outputs

- The formatted text

### Algorithm

1. Split the input string into a list of words.
2. Create an empty list to store the output lines.
3. Create an empty string variable to store the current line.
4. Loop over each word in the list of words.
5. If adding the current word to the current line does not exceed the maximum width, add the word and a space to the current line.
6. If adding the current word to the current line exceeds the maximum width, append the current line to the output lines list, reset the current line to the current word plus a space, and repeat step 5.
7. Append the final current line to the output lines list.
8. Create an empty string variable to store the final output.
9. Loop over each line in the output lines list.
10. If the line ends with a comma, remove the comma and add a newline character.
11. Append the line (with or without the comma) to the final output string.
12. Return the final output string.

