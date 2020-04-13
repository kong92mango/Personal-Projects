
# Part 1

student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

stdDic = {}
for item in student_course_pairs_1:
    try:
        stdDic[item[0]].append(item[1])
    except:
        stdDic[item[0]] = [item[1]]


def FindPair(pair):
    course1 = stdDic[str(pair[0])]
    course2 = stdDic[str(pair[1])]
    shared =  set(course1).intersection(course2)
    return shared

# print(FindPair([94, 25]))



all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
]

dic = {}
for pair in all_courses:
    if pair[0] not in dic:
        dic[pair[0]] = [], [pair[1]]
    else:
        dic[pair[0]][1].append(pair[1])
    if pair[1] not in dic:
        dic[pair[1]] = [pair[0]], []
    else:
        dic[pair[1]][0].append(pair[0])

basics = []
for course in dic:
    if dic[course][0] == []:
        basics.append(course)

print(basics)
allPaths = []

def findChains(basic, out=[]):
    out.append(basic)
    if dic[basic][1] == []:
        out1 = []
        for item in out:
            out1.append(item)
        allPaths.append(out1)
    else:
        for nextCourse in dic[basic][1]:
            findChains(nextCourse, out)
    out.pop()
    return

findChains("Creative Writing")

def findMidCourse(paths):
    out = []
    for path in paths:
        if len(path)%2 == 1:
            out.append(path[len(path)//2])
        else:
            out.append(path[len(path)//2-1])
    return out

print(allPaths)
print(findMidCourse(allPaths))
