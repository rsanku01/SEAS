def read_int(minimum):
    minimum = int(input('Enter a positive integer: '))
    while minimum <= 99:
        minimum = int(input('Number must be more than 3 digits: '))
    return(minimum)

#print(read_int(0))


def compute_inverse(minimum):
    revs_number = str(minimum)[::-1]

    return revs_number

minimum = int(input('Enter a positive integer: '))

print(f'The inverse of: {minimum} is {compute_inverse(minimum)}')



 




   
