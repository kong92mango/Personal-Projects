
intervals1 =[[1300, 1500], [930, 1200],[830, 845],[830,930]]

def insertable(intervals1, new):
    start = new[0]
    end = new[1]
    for time in intervals1:
        if time[0] >= end or time[1] <= start:
            continue
        else:
            return False
    return True


print(insertable(intervals1,[820,830]))
print(insertable(intervals1,[1450,1500]))


def mergeIntervals(intervals):
    sortedInt = sorted(intervals, key = lambda x: x[0])
    mergedInt = [sortedInt[0]]
    for inter in sortedInt:
        if inter[0] <= mergedInt[-1][1]:
            mergedInt[-1][1] = inter[1]
        else:
            mergedInt.append(inter)
    return mergedInt
print(mergeIntervals(intervals1))


def freeTime(intervals):
    start = 0
    end = 2359
    freeTime = []
    for i, v in enumerate(intervals):
        if i == 0:
            if v[0] > start:
                freeTime.append([start, v[0]])
        else:
            freeTime.append([intervals[i-1][1], v[0]])
        if i == len(intervals) -1:
            if v[1] < end:
                freeTime.append([v[1], end])
    return freeTime

print(freeTime(mergeIntervals(intervals1)))




rooms = {
  "Phone Booth":     {"size":  6},
  "War Room":        {"size":  6},
  "Conference Room": {"size": 12}
}

meetings1 = {
  "Standup": {"size":  4, "start": 1230, "end": 1300},
  "Scrum":   {"size":  6, "start": 1230, "end": 1330},
  "UAT":     {"size": 10, "start": 1300, "end": 1500}
}

meetings2 = {
  "Manager 1:1": {"size": 2, "start":  900, "end": 1030},
  "Budget":      {"size": 4, "start":  900, "end": 1000},
  "Forecasting": {"size": 6, "start":  900, "end": 1100},
  "SVP 1:1":     {"size": 2, "start": 1000, "end": 1030},
  "UX Testing":  {"size": 4, "start": 1115, "end": 1130}
}

def task3(roomsDict,meetingsDict):
    rooms,meetings = [],[]
    res = {}
    for room,info in roomsDict.items():
        rooms.append([room,info["size"],[]])
    for meeting,info in meetingsDict.items():
        meetings.append([meeting,info["size"],[info["start"],info["end"]]])
    rooms.sort(key = lambda x: x[1])
    meetings.sort(key = lambda x: x[1],reverse=True)
    print(rooms, meetings)
    for meeting in meetings:
        for i, room in enumerate(rooms):
            if room[1]>=meeting[1] and insertable(room[2],meeting[2]):
                room[2].append(meeting[2])
                res[meeting[0]] = room[0]
                break
            if i == len(rooms)-1:
                return "Impossible"
    return res

print(task3(rooms, meetings2))
