# Decodes a message from a file

This function reads an encoded message from a file and returns its decoded version as a string. The input file format is:

    3 love
    6 computers
    2 dogs
    4 cats
    1 I
    5 you

The function should return the decoded message as a string: "I love computers"

## Usage

Here is an example of how to use the function:

    message_file = 'message.txt'
    decoded_message = decode(message_file)
    print(decoded_message)

## How it works

The function does the following:

1. Reads the file and stores the numbers in a list, and the corresponding words in another list.
2. Sorts the list of numbers in ascending order.
3. Creates a pyramid structure using the numbers, where the smallest number is 1, and the numbers increase consecutively.
4. Finds the word corresponding to the final number in the pyramid.
5. Uses the words in the pyramid to create the decoded message.
6. Returns the final message.

