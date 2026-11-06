# Create a list of numbers.
# Add an element.
# Remove an element.
# Find maximum and minimum.
# Display the sorted list.
def list_operations():
    nums = [10, 20, 30, 40, 50,30]

    nums.append(60)
    nums.remove(20)

    print("List:", nums)
    print("Maximum:", max(nums))
    print("Minimum:", min(nums))
    print("Sorted:", sorted(nums))

list_operations()

