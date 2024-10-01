# Number of rows for the pyramid
rows = 5

# Loop through the rows
for i in range(1, rows + 1):
    # Print leading spaces
    print(' ' * (rows - i), end='')
    
    # Print stars for the current row
    print('*' * (2 * i - 1))

    
