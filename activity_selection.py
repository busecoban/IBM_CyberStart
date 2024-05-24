def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])
    
    return selected

activities = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
print(activity_selection(activities))  # Output: [(1, 2), (3, 4), (5, 7), (8, 9)]
