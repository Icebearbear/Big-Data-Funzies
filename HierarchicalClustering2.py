# Set the original points
original_points = [0, 1, 3, 7, 10, 14, 16, 24, 30]

# Sorting the list so that the pair_of_smallest_diff algorithm works better
# Since it is only comparing the elements sequentially making it a O(nLog(n))
original_points = sorted(original_points)
cluster = []
cluster2 = []
# find the min distance between two clusters, the min distance between any nodes inside clusters
# Expected output
# []
# [[0, 1], [14, 16]]
# [13]
# [13]
# [[7, 10], [24, 30]]
# [13, 14]


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

        # Insert the new point into a new pairing array and delete the original points
        first_val = original_points[pair[0]]
        sec_val = original_points[pair[1]]
        
        cluster.append([first_val,sec_val])
        del original_points[pair[1]]
        del original_points[pair[0]]
        
        # find distance between 2 clusters , the minimum distance between the nodes inside clusters
        if(len(cluster) > 1):
            print(cluster)
            diff = abs(cluster[0][0] - cluster[1][0])
            for i in cluster[0]:
                for j in cluster[1]:
                    if abs(i-j) < diff:
                        diff = abs(i-j)
            cluster2.append(diff) # add the min distance to anwe array
            del cluster[:] # empty the pairing array

        # Show the points everytime after it is reduced
        print(cluster2)

    return cluster2


print("The final shortest distances are:", main())
