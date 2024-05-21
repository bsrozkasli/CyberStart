import math

# Defining Points
points = [(1, 2), (3, 4), (5, 6), (7, 8)]  # Example: I've defined four points

# Function for Euclidean Distance
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Calculating Distances
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):  # Starting j from i+1 to avoid checking the same points twice
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Finding Minimum Distance
min_distance = min(distances)

print("Minimum distance:", min_distance)
