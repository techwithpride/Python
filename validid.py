aadhar=1111
pan=2345
apaar=6789
ID = int(input("Enter ID: "))
if int(ID) == aadhar:
    print("Valid Aadhar ID")
elif int(ID) == pan:
    print("Valid PAN ID")
elif int(ID) == apaar:
    print("Valid APAAR ID")
else:
    print("Invalid ID! Please enter the correct ID.")