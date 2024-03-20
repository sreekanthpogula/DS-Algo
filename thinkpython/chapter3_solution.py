def right_justify(s):
    n = len(s)
    num_of_spaces = 70 - n
    print(''*num_of_spaces, s)

right_justify('sreekanth'*15)


arg = 'spam'
def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print(arg)
    print(arg)

do_twice(print_twice, arg)
print()

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, arg)


def print_square(lines):
    print(lines)
    print(lines)
    print(lines)
    print(lines)

def grid_plus_line(n_of_columns):
    columns = (' +-----')*n_of_columns + ' +'
    print(columns)

def grid_row(num_of_columns):
    grid_plus_line(num_of_columns)
    
    lines = (' |     ')*num_of_columns + ' |'
    print_square(lines)
    
def grid_rows(num_of_rows, num_of_columns):
    while num_of_rows > 1:
        grid_row(num_of_columns) 
        num_of_rows -=1
      
def grid(num_of_rows, num_of_columns):
    grid_row(num_of_columns)
    grid_rows(num_of_rows, num_of_columns)
    grid_plus_line(num_of_columns)
    
    
grid(2, 2)
grid(4, 4)
print()
