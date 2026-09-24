# Emily Fehlberg
# 09/23/2026
# Lab Prep Assignment - Week 5

# EXTRACT ID NUMBER
# add variable and data:
id = "id:20952408"

# write code to extract numeric parts:
clean_id = id.strip()
numeric_str = clean_id.split(":")[1]
numeric_id = int(numeric_str)

# print original ID and data type variable:
print("Original ID", id, "| Type", type(id))
print("Numeric ID", numeric_id, "| Type", type(numeric_id))

print("-" * 20)


# DECONSTRUCT ADDRESS
# add variable and data:

address = "123 Main St., Iowa City, IA 52241"

# write code to extract state:
state_zip = address.split(
    ",",
)[2].strip()
state = state_zip.split()[0]

# print state variable:
print("State:", state)

print("DONE!")
