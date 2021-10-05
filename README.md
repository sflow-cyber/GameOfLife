# GameOfLife

main.py contains a version of Conways game of life that I created recently.
main.py can be executed or imported.
If main.py is executed directly, a small user interface will ask for the size of the grid and the probability that each cell is alive at start.
The window for the grid is (by default) 800x800px.
By default, the simulation is run until all cells are dead. To stop the simulation, user must send KeyboardInterrupt.
If main.py is exported, the class grid is made available.
Note that, if grid is imported and used in another context, it is possible to run the simulation a predefined number of times.