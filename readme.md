# Python Password Generator

This is a random password generator written in Python. It asks you for the number of letters, numbers, and symbols and then outputs a randomly generated password.

## How It's Made

The script does the following:

1. Asks the user for how many letters, symbols, and numbers they want their password to include.
2. These values are stored in three variables.
3. These variables are fed into three separate functions to generate random letters, symbols, and numbers.
4. Each list of random characters are combined into one list.
5. The list is then shuffled via the random library.
6. The shuffled list is joined into a string and printed to the console.

## Lessons Learned

The script was pretty straightforward for me to build. The only issue I ran into was learning how random.shuffle() works. I was tryint to store it to a variable but that was not working.

The main lesson learned from this was just breaking it down into separate pieces to solve and then bringing them all back together in the end.
