# read_inventory_file.py

def read_inventory(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())

read_inventory('inventory.txt')
