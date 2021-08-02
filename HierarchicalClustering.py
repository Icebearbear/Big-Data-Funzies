# Set the original points
original_points = [0, 1, 3, 7, 10, 14, 16, 24, 30]

# Sorting the list so that the pair_of_smallest_diff algorithm works better
# Since it is only comparing the elements sequentially making it a O(nLog(n))
original_points = sorted(original_points)

# Expected output
# [0, 1, 3, 7, 10, 14, 16, 24, 30]
# [0.5, 3, 7, 10, 14, 16, 24, 30]
# [0.5, 3, 7, 10, 15, 24, 30]
# [1.75, 7, 10, 15, 24, 30]
# [1.75, 8.5, 15, 24, 30]
# [1.75, 8.5, 15, 27]
# [1.75, 8.5, 15, 27]
# [1.75, 11.75, 27]
# [6.75, 27]
# [6.75, 27]
# [16.875]


def pair_of_smallest_diff(numbers):
    # Initialize difference as difference between the first and second elements
    diff = numbers[1] - numbers[0]

    # Set elements as first and second element since that is the initial diff
    elements = (0, 1)

    for i in range(1, len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < diff:
            diff = numbers[i + 1] - numbers[i]
            elements = (i, i + 1)

    # Return the elements that have the smallest difference in the whole list
    return elements


def main() -> float:

    while len(original_points) > 1:
        # Get a pair of points from the list that has the smallest difference
        pair = pair_of_smallest_diff(original_points)

        # Get new point by getting the center of the pair
        new_point = (original_points[pair[0]] + original_points[pair[1]]) / 2

        # Insert the new point into the list and delete the original points
        original_points[pair[0]] = new_point
        del original_points[pair[1]]

        # Show the points everytime after it is reduced
        print(original_points)

    # The last element in the list after reducing down is the middle point
    return original_points[0]


print("The final middle point is:", main())
