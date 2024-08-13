def reverse_binary_file(input_file_path, output_file_path):
    # Open the input binary file in read mode and read the content
    with open(input_file_path, 'rb') as input_file:
        data = input_file.read()

    # Reverse the content
    reversed_data = data[::-1]

    # Write the reversed content to the output binary file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(reversed_data)

# Example usage
input_file_path = 'example.bin'
output_file_path = 'reversed_example.bin'
reverse_binary_file(input_file_path, output_file_path)
