# file_operations.py
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data)
