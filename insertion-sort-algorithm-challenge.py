# Function for the insertion sort algorithm itself
def insertion_sort(user_list):
    holder = []
    for i in range(1, len(user_list)):
        j = i
        while user_list[j-1] > user_list[j] and j > 0:
            user_list[j-1], user_list[j] = user_list[j], user_list[j-1]
            holder += user_list
            j -= 1
    return holder

# Function to print the steps of the insertion sort algorithm, using lists to do so
def show_steps(orig_list, something):
    a_list = []
    t = 0
    q = len(orig_list)
    for i in range(int(len(something)/len(orig_list))):
        while t <= len(something)-len(orig_list):
            a_list.append(something[t:q])
            t += len(orig_list)
            q += len(orig_list)
    return a_list

# Convert list formats to string for correct formatting
def string_converter_original(arr):
    x = [str(x) for x in arr]
    separator = ', '
    output = separator.join(x)
    return f"{output}"

# Function to generate the final output of the insertion sort algorithm
def final_output(final_list):
    for i in range(len(final_list)):
        string_final = string_converter_original(final_list[i])
        print(f"Swap{i+1} :", string_final)
    print("Sorted Listv:", string_converter_original(final_list[-1]) )

# Small function to find the mean of the list of numbers
def mean(nums_list):
    return float(sum(nums_list)) / max(len(nums_list), 1)

# User prompt for the input script
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
            new_list = insertion_sort(a_list)
            almost_done = show_steps(a_list,new_list)
            print("Original List:", string_converter_original(a_list))
            final_output(almost_done)
            print("Mean Value:", mean(a_list))
    except:
        print("Sorry, I did not recognize that, please try again.")
