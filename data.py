import math
from typing import Any

# Representation of time as hours, minutes, and seconds
class Time:
    # Initialize a new Point object.
    # input: hour as an int
    # input: minute as an int
    # input: second as an int
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    # Purpose: Determine if two Time objects are equal by comparing their hour, minute, and second values.
    # Input: other (Any) - The object to compare against the current Time object.
    # Output: (bool) - True if the two Time objects are equal, False otherwise.
    def __eq__(self, other:Any) -> bool:
        return (type(other) == Time and self.hour == other.hour
            and self.minute == other.minute
            and self.second == other.second)

    # Purpose: Return a string representation of the Time object,
    # which includes the hour, minute, and second in a formatted manner.
    # Output: (str) - A string that represents the Time object in the format
    # "hour = {hour}, minute = {minute}, second = {second}".
    def __repr__(self) -> str:
        return ("hour = {}, minute = {}, second = {}".format(
            self.hour, self.minute, self.second))

    # Provide a developer-friendly string representation of the object.
    # input: Time for which a string representation is desired. 
    # output: string representation


    # Compare the Time object with another value to determine equality.
    # input: Time against which to compare
    # input: Another value to compare to the Time
    # output: boolean indicating equality




# Representation of a two-dimensional point.
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    # Provide a developer-friendly string representation of the object.
    # input: Point for which a string representation is desired. 
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)


    # Compare the Point object with another value to determine equality.
    # input: Point against which to compare
    # input: Another value to compare to the Point
    # output: boolean indicating equality
    def __eq__(self, other:Any) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))
