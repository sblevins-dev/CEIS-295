# Name: Stephen Blevins
# Date: 06/10/2022

from BinarySearchTree import BinarySearchTree
from Client import Client
from datetime import date
import time     # use to time the code executions
import random
import sys

# display author's name and the date in the output
print("Name: ", "Stephen Blevins")
print("Date: ", date.today())
print()

# create a list
clients = []

# read records into the list
input_file_name = "ClientData.csv"
with open(input_file_name) as infile:
    for line in infile:
        # split the line based on the commas
        s = line.split(',')
        client_id = int( s[0] )     # convert to integer
        f_name = s[1]
        l_name = s[2]
        phone = s[3]
        email = s[4]
        # create client object using data from the line
        clt = Client(client_id, f_name, l_name, phone, email)
        # add the client object to the list
        clients.append(clt)

# how many client objects do we have?
num_records = len(clients)

# create the Binary Search Tree to test real-world speeds
my_bst = BinarySearchTree()

# Scenario 1: Printer Queue or Call Queue or Service Queue
section_title = "Scenario: Printer Queue or Call Queue or Service Queue"
print(section_title)
print("-" * len(section_title))

# how long does it take to add the client records to the BST
start_time = time.time()

for i in range(num_records):
    my_bst.insert(clients[i])

end_time = time.time()
total_time = end_time - start_time
print("Seconds to add records: {:.6f}".format(total_time)) # .6f means six decimal places

# how long does it take to remove records from the front (smallest) of the BST
start_time = time.time()

for i in range(num_records):
    my_bst.remove_minimum()

end_time = time.time()
total_time = end_time - start_time
print("Seconds to remove records: {:.6f}".format(total_time)) # .6f means six decimal places

# Scenario 2: Customer Service Center
answer = input("Continue (y/n)? ")
if answer.lower() != "y":
    sys.exit()      # end the application

section_title = "Scenario: Customer Service Center"
print(section_title)
print("-" * len(section_title))

# add clients to the BinarySearchTree
for i in range(num_records):
    my_bst.insert(clients[i])

# how long does it take to randomly display 1000 client records
start_time = time.time()

for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print( my_bst.search(Client(random_num)))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to display 1000 random records: {:.6f}".format(total_time)) # .6f means six decimal places

# Scenario 3: Call Center
answer = input("Continue (y/n)? ")
if answer.lower() != "y":
    sys.exit()      # end the application

section_title = "Scenario: Call Center"
print(section_title)
print("-" * len(section_title))

# add clients to the BinarySearchTree
for i in range(num_records):
    my_bst.insert(clients[i])

# how long does it take to add more client records,
# randomly display 1000, and randomly remove 1000 records from the BST?
start_time = time.time()

# add records
current_id = 100001 + num_records + 1
for i in range(1000):
    my_bst.insert(Client(current_id))
    current_id += 1

# display records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    print( my_bst.search(Client(random_num)))

# remove 1000 random records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + num_records
    random_num = random.randint(smallest_id, largest_id)
    my_bst.remove(Client(random_num))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to add records,")
print("display 1000 random records,")
print("and remove 1000 random records: {:.6f}".format(total_time)) # .6f means six decimal places



















