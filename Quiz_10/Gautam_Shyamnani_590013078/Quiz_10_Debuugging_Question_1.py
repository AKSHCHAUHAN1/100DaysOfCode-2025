def activity_selection(start, end):
    n = len(start)
    activities = []

    # Combine start and end times with index
    for i in range(n):
        activities.append((start[i], end[i], i))

    # ✅ Sort activities by end time (greedy choice)
    activities.sort(key=lambda x: x[1])

    selected = [activities[0]]
    last_end = activities[0][1]

    # Select non-overlapping activities
    for i in range(1, n):
        if activities[i][0] >= last_end:
            selected.append(activities[i])
            last_end = activities[i][1]

    return len(selected)

# 🔍 Test case
start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]

result = activity_selection(start, end)
print(f"Maximum activities: {result}")
