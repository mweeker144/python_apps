# Variable to hold a list of passes for later output.
loop_counter = []
# Function to capture and transform the format of the various passes and the original list
def print_steps(arrs, num):
    x = [str(x) for x in arrs]
    separator = ', '
    output = separator.join(x)
    loop_counter.append(num)
    if num == 0:
        return f"Original List: {output}"
    else:
        return f"Pass {num}: {output}"

# Repeating function to conver the original list as printing this twice is a technical requirement.
def string_converter_original(arr):
    x = [str(x) for x in arr]
    separator = ', '
    output = separator.join(x)
    return f"Original List: {output}"

# Additonal function to format the sorted list.
def string_converter_sorted(arr):
    x = [str(x) for x in arr]
    separator = ', '
    output = separator.join(x)
    return f"Sorted List: {output}"

# Main bubble sort function. This does call other function in order to show the lists in a new format and at various passes.
def bubble_sort(arr):
    t = True
    org_list = string_converter_original(arr)
    while t:
        for i in range(len(arr)):
            no_swaps = True
            if i < len(arr)-1:
                print(print_steps(arr, i))
            for j in range(0, (len(arr)-1)):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                    no_swaps = False
            if no_swaps:
                t = False
                break
    print(org_list)
    print(string_converter_sorted(arr))
    return f"Number of Passes: {loop_counter[-1]}"

# User entry loop to trigger sorting algorithm and various outputs.
keep_running = True
while keep_running: 
    try:
        user_input = input("Enter a comma separated list of numbers for sort. Type 'exit' at any time to end the program.\n")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            keep_running = False
            break
        else:
            a_list = user_input.split(",")
            a_list = [int(x) for x in a_list]
            print(bubble_sort(a_list))
    except:
        print("Sorry, I did not recognize that, please try again.")


