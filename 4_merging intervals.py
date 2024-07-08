import ast

def mergeIntervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  
            merged[-1] = (last[0], max(last[1], current[1]))  
        else:
            merged.append(current)

    return merged


intervals = ast.literal_eval(input())

result = mergeIntervals(intervals)
print(result)
