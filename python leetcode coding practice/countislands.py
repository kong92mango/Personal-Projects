mat = [
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0, 1, 1],
  [0, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 0, 1, 1],
  [1, 0, 1, 0, 1, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [0, 1, 0, 1, 1, 1, 0],
]

count = 0
islands = []

def searchLand(x , y):
    islands.append([])
    if mat[y][x] == 0:
        mat[y][x] = 1
        islands[-1].append([y,x])
        maxx = len(mat[0])-1
        maxy = len(mat)-1
        if x < maxx and mat[y][x+1] == 0:
            searchLand(x+1,y)
        if x > 0 and mat[y][x-1] == 0:
            searchLand(x-1,y)
        if y < maxy and mat[y+1][x] == 0:
            searchLand(x,y+1)
        if y > 0 and mat[y-1][x] == 0:
            searchLand(x,y-1)
        if mat[y-1][x] == 0 and mat[y+1][x] == 0 and mat[y][x+1] == 0 and mat[y][x-1] == 0:
            count += 1

for y in range(len(mat)):
    for x in range(len(mat[0])):
        if mat[y][x] == 0:
            searchLand(x, y)
print(islands)
