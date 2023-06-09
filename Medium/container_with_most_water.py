'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container. '''


def maxArea(height):
    point1, point2 = 0, len(height) - 1
    max_water = 0
    while point1 < point2:
        if height[point1] < height[point2]:
            area = height[point1] * (point2 - point1)
            point1+=1
        else:
            area = height[point2] * (point2 - point1)
            point2-=1
        if max_water < area:
            max_water = area
    return max_water
