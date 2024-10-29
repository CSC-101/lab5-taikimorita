import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
# Purpose: Add two Time objects and return a new Time object that represents
# the sum of the two times, ensuring that the seconds and minutes are in the range of 0-59.
# Input:
#   time1 (data.Time): The first Time object to be added.
#   time2 (data.Time): The second Time object to be added.
# Output:
#   (data.Time) - A new Time object representing the total time
def time_add(time1: data.Time, time2: data.Time) -> data.Time:
    total_seconds = time1.second + time2.second
    total_minutes = time1.minute + time2.minute
    total_hours = time1.hour + time2.hour

    if total_seconds >= 60:
        total_seconds -= 60
        total_minutes += 1

    if total_minutes >= 60:
        total_minutes -= 60
        total_hours += 1

    return data.Time(total_hours, total_minutes, total_seconds)

# Part 4
# Purpose: Check if the elements of the provided list are in strictly
# descending order. An empty list or a list with one element is considered to be in descending order.
# Input:
#   lst (list[float]): A list of floating-point numbers to be checked.
# Output:
#   (bool) - Returns True if the list is in strictly descending order, otherwise returns False.
def is_descending(lst: list[float]) -> bool:
    if len(lst) <= 1:
        return True

    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            return False

    return True

# Part 5
# Purpose: Find the index of the largest integer in a specified range within a list.
# If the range is invalid (lower > upper), return None. If the adjusted range goes
# out of bounds, adjust the indices accordingly.
# Input:
#   nums (list[int]): A list of integers from which to find the largest value.
#   lower (int): The lower index (inclusive) of the range to consider.
#   upper (int): The upper index (inclusive) of the range to consider.
# Output:
#   (Optional[int]) - Returns the index of the largest value found in the specified
#                     range or None if the range is invalid or the list is empty.
def largest_between(nums: list[int], lower: int, upper: int) -> Optional[int]:
    if lower > upper:
        return None

    adjusted_lower = max(0, lower)
    adjusted_upper = min(len(nums) - 1, upper)

    if adjusted_lower > adjusted_upper:
        return None

    largest_index = adjusted_lower
    for i in range(adjusted_lower, adjusted_upper + 1):
        if nums[i] > nums[largest_index]:
            largest_index = i

    return largest_index

# Part 6
# Purpose: Determine the index of the point that is furthest from the origin (0,0).
# The distance is calculated using the squared distance formula to avoid unnecessary
# computation of the square root. If the list of points is empty, return None.
# Input:
#   points (list[data.Point]): A list of Point objects, each representing a point in 2D space.
# Output:
#   (Optional[int]) - Returns the index of the point that is furthest from the origin or None if the list is empty.
def furthest_from_origin(points: list[data.Point]) -> Optional[int]:
    if not points:
        return None

    max_distance_squared = -1
    furthest_index = -1

    for index, point in enumerate(points):
        distance_squared = point.x ** 2 + point.y ** 2

        if distance_squared > max_distance_squared:
            max_distance_squared = distance_squared
            furthest_index = index

    return furthest_index
