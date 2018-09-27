# aStar
To run the program use `python display.py` or `python display2.py` for task 2.
To change which board is used you must change the string in the main call in display.py and display2.py
You might have to install tkinter. `sudo apt install python3-tk`

## Implementation
We have implemented our own version of a*, using the euclidian distance as the heuristic function. We use the heapq libary to organize our priority-queue and each Node keeps track of its neighbours. We thought this was easier than keeping track of it in a adjancency list or matrix.  


## Visualization
For visualization we use the python module Tkinter. Tkinter is a python interface to the Tk GUI toolkit which is available on most unix systems. 

It is a simple no hassle tool for creating simple visulazations. We created a grid by looping through the nodes generating rectangles. The shortest path is designated by the golden path.

### 1-1:
![1-1](/visualizations/1-1.png)

### 1-2:
![1-2](/visualizations/1-2.png)

### 1-3:
![1-3](/visualizations/1-3.png)

### 1-4:
![1-1](/visualizations/1-1.png)

### 2-1:
![2-1](/visualizations/2-1.png)

### 2-2:
![2-2](/visualizations/2-2.png)

### 2-3:
![2-3](/visualizations/2-3.png)

### 2-4:
![2-4](/visualizations/2-4.png)
