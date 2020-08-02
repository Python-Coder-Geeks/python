plang = {"Python": 1, "Java": 3, "Go": 2, "Kotlin": 4}
print(plang)
for i in plang:
    print(i)
del plang["Java"]

print("   ")
plang["Go"] = 2
plang["Kotlin"] = 3

print(plang)

plang["C"] = 3
plang["Kotlin"] = 4
print(plang)
print("    ")
for j in plang:
    print(j)
print("   ")
print("End of Sample Code")
 
