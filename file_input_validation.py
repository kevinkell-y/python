
# Get a .csv file from the user, confirm that it exists
csv_file = input("Enter .csv file: ")

try:
    user_csv = open(csv_file, "r")    
except: 
    print("File cannot be opened: ", csv_file)
    exit()


# Checkpoint
print(f"Success, {csv_file} is a real file.")