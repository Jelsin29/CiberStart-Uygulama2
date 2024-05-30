# CyberStart Uygulama2: Minimum Euclidean Distance

This Python program calculates the minimum Euclidean distance between points entered by the user. It is a homework assignment from the IBM ile kodluyoruz: CyberStart program.

## Features

- Asks the user to enter the number of points
- Asks the user to enter the coordinates of each point
- Calculates the Euclidean distance between every pair of points
- Finds the minimum Euclidean distance among all pairs
- Prints the minimum Euclidean distance

## Requirements

- Python 3.x
- math module

## Usage

1. Run the Python script.
2. Enter the number of points you want to input.
3. For each point, enter the x and y coordinates separated by a space.
4. The program will calculate and print the minimum Euclidean distance among all pairs of points.

## Example

How many points are you going to enter? 3

1. Enter the coordinates of each point (x y) separated by a space: 0 0
2. Enter the coordinates of each point (x y) separated by a space: 3 4
3. Enter the coordinates of each point (x y) separated by a space: 6 8
   Minimum Euclidean distance: 5.0

In this example, the minimum Euclidean distance between the three points (0, 0), (3, 4), and (6, 8) is 5.0.

## Functions

`getPoints()` : Asks the user to enter the number of points and their coordinates. Returns a list of tuples representing the points.

`euclideanDistance(point1, point2)` : Calculates the Euclidean distance between two points using the formula `sqrt((x2 - x1)^2 + (y2 - y1)^2)`.

`findMinimumDistance(points)` : Finds the minimum Euclidean distance among all pairs of points in the given list.

`main()` : The main function that calls the other functions and handles the program flow.

## Note

This program assumes that the user enters valid input (numbers for coordinates). Error handling for invalid input is not implemented.
