import math

def getPoints():
    points = []
    n = int(input("How many points are you going to enter? "))
    for i in range(n):
        x, y = map(float, input(f"{i+1}. Enter the coordinates of each point (x y) separated by a space: ").split())
        points.append((x, y))
    return points

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def findMinimumDistance(points):
    minDistance = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            if distance < minDistance:
                minDistance = distance
    return minDistance

def main():
    points = getPoints()
    if len(points) > 1:
        minDistance = findMinimumDistance(points)
        print(f"Minimum Euclidean distance: {minDistance}")
    else:
        print("There are not enough points to calculate the distance.")

if __name__ == "__main__":
    main()
