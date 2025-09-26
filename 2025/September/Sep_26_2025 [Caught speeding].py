'''
Caught Speeding
Given an array of numbers representing the speed at which vehicles were 
observed traveling, and a number representing the speed limit, return an 
array with two items, the number of vehicles that were speeding, followed by 
the average amount beyond the speed limit of those vehicles.
    If there were no vehicles speeding, return [0, 0]
'''

def speeding(speeds, limit):
    over_speeders = [x for x in speeds if x > limit]
    if over_speeders:
        avg_overspeed = (sum([x-limit for x in over_speeders]))/len(over_speeders)
        result = [len(over_speeders), avg_overspeed]
        
    else:
        result = [0,0]
    return result

print(speeding([50, 60, 55], 60)) #should return [0, 0].
print(speeding([58, 50, 60, 55], 55)) #should return [2, 4]
print(speeding([61, 81, 74, 88, 65, 71, 68], 70)) #should return [4, 8.5]
print(speeding([100, 105, 95, 102], 100)) #should return [2, 3.5]
print(speeding([40, 45, 44, 50, 112, 39], 55)) #should return [1, 57]