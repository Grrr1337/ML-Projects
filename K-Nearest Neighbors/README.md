# KNN Interactive Visualization
This is a demo that displays an interactive 2D and 3D visualization of the **K-Nearest** Neighbors (KNN) algorithm. The code utilizes the `numpy`, `matplotlib`, and `tkinter` libraries to create a graphical user interface (GUI) that allows users to move a point in the 2D or the 3D space and observe its classification based on the KNN algorithm.

## Demo
### 2D K-Nearest Neighbors
![KNN Demo 2D](KNN%20Demo%202D.gif)
### 3D K-Nearest Neighbors
![KNN Demo 3D](KNN%20Demo%203D.gif)

## Getting Started

### Prerequisites
One must make sure that has the following Python libraries installed:

```bash
pip install numpy matplotlib
``` 

### Running the Code
Simply run the provided Python script:
```bash
python main.py
```

## How it works

### 2D K-Nearest Neighbors
1. The initial 2D visualization displays points in two categories: "blue" and "red."
2. A new point, represented by a star marker, is introduced at coordinates [3, 3].
3. Use the mouse to interactively move the new point in the 2D space.
4. The visualization updates in real-time, showing the classification of the moved point based on KNN.

### 3D K-Nearest Neighbors
1. The initial 3D visualization displays points in two categories: "blue" and "red."
2. A new point, represented by a star marker, is introduced at coordinates [3, 3, 4].
3. Use the keys [W/A/S/D/Q/E] to move the new point in the X, Y, and Z directions interactively.
4. The visualization updates in real-time, showing the classification of the moved point based on KNN.

## Code Structure
- The `KNearestNeighbors` class is implemented for the KNN algorithm, allowing fitting and prediction on given points.
- The `euclidean_distance` function calculates the Euclidean distance between two points.
- The GUI is created using `tkinter`, and user input is captured through the on_key function.
- Matplotlib is used to create the 2D or the 3D visualization, and the plot is updated dynamically as the point is moved.

## Dependencies
- `numpy`: Used for numerical operations.
- `matplotlib`: Utilized for creating 3D visualizations.
- `tkinter`: Used for GUI components and capturing keyboard events.

## Notes
- The color-coding is as follows: "blue" points are represented by a blue color, "red" points are represented by a red color, and the new point's classification is indicated by a distinct color (red or blue).

The goal is to explore and interact with the visualization to gain insights into how the KNN algorithm point classification in the 2D or 3D space.

## Author
Vladimir Balabanov ( **Grrr1337** )

## License
This project is licensed under the MIT License.

