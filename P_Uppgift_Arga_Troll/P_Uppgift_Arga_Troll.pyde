gridSize = 6
grid = [ [-1]*gridSize  for n in range(gridSize)] # list comprehension
grid[0][0] = 1
#grid[5][5] = 1

w = 70 # width of each cell

def setup():
    size(800,600)
    
def draw():
    
    x,y = 0,0 # starting position

    for row in grid:
        for col in row:
          if col == 1:
              fill(0,255,0)
          else:
              fill(255)
          rect(x, y, w, w)
          x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge
        
        
def mousePressed():
   # for row in grid:
    #    for col in row:
     #       if col == 0:
                grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]
                
