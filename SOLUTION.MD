About the project
* `The function path_exists is implemented`
* `Run the function by providing the various grid and queries`
* `File has been saved as Amara_Datta_Sachidananda_solve.py`

About Implementation
* The given problem could have been implemeted in two different ways
* The first method was use to use recursion which would iterate all the way to the end
* The second method was to implement the a* search algorithm, which improves the performance
* In the program algorithm uses the hueristic value to find the more efficient route through the matrix
* Based on the total cost f(n) = g(n) + h(n) the next cells to be traversed is calculated
* g(n) is the cost to move from the start to the current cell
* h(n) = abs((X_current - X_end)*10) +((Y_current - Y_end)*10)
* The next path to be taken is calculated by checking all the surrounding four cells (if all are present)
* Children cell, if we are to move into it, must contain the value 1
* It should also ideally have less hueristic when compared to others
* Afer we find out the children we iterate through the children to see if we can find the end cell


