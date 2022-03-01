# Function to take nested list as input
def list_creater(arr):
    lst = []
    n = int(input(f"Enter number of elements in {arr} : "))
    for i in range(0, n):
        ele = [int(input(f'enter the 1st element in {arr}[{i}]: ')),
               int(input(f'enter the 2nd element in {arr}[{i}]: '))]
        lst.append(ele)
    return lst


arr1 = list_creater('arr1')
arr2 = list_creater('arr2')
output = []


def print_intervals(arr1, arr2):
    # i and j pointers for arr1 and arr2 respectively
    i = j = 0

    n = len(arr1)
    m = len(arr2)

    # Loop through all intervals unless one of the interval gets exhausted
    while i < n and j < m:

        # Left bound for intersecting segment
        l = max(arr1[i][0], arr2[j][0])

        # Right bound for intersecting segment
        r = min(arr1[i][1], arr2[j][1])

        # If segment is valid, append it to the output list
        if l <= r:
            output.append([l, r])

        # If i-th interval's right bound is smaller increment i else increment j
        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1
    print('The common intervals between the two lists of time intervals is', output)


print_intervals(arr1, arr2)
