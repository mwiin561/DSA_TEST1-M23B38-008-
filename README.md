# DSA_TEST1-M23B38-008-

##EXPLANATION FOR NUMBER 2

Step 1: Creating two separate lists of names
We are creating two separate lists of names, one for Catholic martyrs and one for Anglican martyrs. These lists will contain the names of the martyrs that we want to check if they are in both lists.

Step 2: Removing duplicates from the lists
We are using the built-in `set()` function to remove any duplicate names from both lists. This is because we don't want to count the same name twice.

Step 3: Creating a function to count the number of martyrs
We are creating a function called `martyr_count` that takes in a name as an argument. The function checks if the name is in the list of Catholic martyrs or Anglican martyrs. If it is, the function returns the group (Catholic or Anglican) to which the martyr belongs. If the name is not in either list, the function returns "Not a martyr".

Step 4: Using the function to determine the group of a martyr
We are using the `martyr_count` function to determine the group of a martyr named "Kizito". We pass the name "Kizito" as an argument to the function, and it returns "Catholic".

Step 5: Creating a function to check if a name is a martyr
We are creating a function called `is_martyr` that takes in a name as an argument. The function checks if the name is in either the list of Catholic martyrs or Anglican martyrs. If it is, the function returns True. If the name is not in either list, the function returns False.


Specific libraries used:

* None. We are using built-in Python functions and data structures.
