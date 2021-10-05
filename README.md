# GameOfLife

main.py contains a version of Conways game of life that I created recently.
main.py can be executed or imported.
If main.py is executed directly, a small user interface will ask for the size of the grid and the probability that each cell is alive at start.
The window for the grid is (by default) 800x800px.
By default, the simulation is run until all cells are dead. To stop the simulation, user must send KeyboardInterrupt.
If main.py is exported, the class grid is made available.
Note that, if grid is imported and used in another context, it is possible to run the simulation a predefined number of times.

GameOfLife.xlsm is an MS Excel file that contains another version of the Game of Life that I created 4-5 years ago.
The first worksheet is used as UI and to display the grid.
In order to change the cell from living to dead just directly change their colors. A living cell is yellow, a dead cell is white.
You can always delete the entire grid and create a randomly populated grid.
The code can be observed, debugged, and changed under Developer Tools > Visual Basic 
