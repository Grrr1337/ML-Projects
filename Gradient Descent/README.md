# Gradient Descent

**Gradient Descent** is a fundamental optimization algorithm widely used in machine learning and numerical optimization. Its primary purpose is to minimize a given function iteratively by adjusting the parameters in the direction of the steepest decrease (negative gradient). This iterative approach allows the algorithm to find the minimum (or maximum) of a function efficiently.


This is a **demonstration** that include both 2D and 3D gradient descent scenarios.

#### Gradient Descent Purpose:
The primary purpose of Gradient Descent is to find optimal parameter values that minimize a given cost function. In the context of machine learning:

- **Model Training**: In machine learning, models are trained by minimizing a cost function that measures the difference between predicted and actual outcomes. Gradient Descent adjusts the model's parameters to minimize this discrepancy.

- **Neural Network Training**: In deep learning, Gradient Descent is a cornerstone for training neural networks. It adjusts the weights and biases of the network to minimize the error between predicted and true values.

- **Global Optimization**: Beyond machine learning, Gradient Descent is used in various optimization problems, such as finding the global minimum of complex functions in physics, engineering, and economics.

#### Gradient Descent Key Concepts:
- **Optimization**: Gradient Descent is employed to optimize a cost or objective function, which represents the performance or error of a model or system.

- **Derivative**: The algorithm relies on the derivative (gradient) of the function with respect to its parameters. The derivative provides the direction of the steepest ascent, and moving in the opposite direction decreases the function value.

- **Learning Rate**: The learning rate determines the step size during each iteration. It is a crucial hyperparameter that influences the convergence speed and stability of the algorithm. A proper learning rate ensures a balance between quick convergence and avoiding overshooting the minimum.

- **Iterations**: Gradient Descent iteratively updates the parameters until convergence. Convergence occurs when the algorithm reaches a point where further adjustments do not significantly improve the function's value.

## Demo
#### 2D Gradient Descent Visualization
![2D Gradient Descent](2D%20Gradient%20Descent.gif)

#### 3D Gradient Descent Visualization
![3D Gradient Descent](3D%20Gradient%20Descent.gif)

## 2D Gradient Descent
The 2D gradient descent demonstration focuses on optimizing a given function by iteratively adjusting the input parameter using gradient descent. The script provides a visual representation of the process, displaying the function's curve and the movement of the optimization algorithm over time.
It uses the matplotlib library for plotting.

## 3D Gradient Descent
The 3D gradient descent demo extends the optimization scenario to a three-dimensional space. It explores the optimization of a specific function using gradient descent, showing how the algorithm navigates through the landscape to find the optimal solution.
 
## How It Works
The visual explanations are inspired by the tutorial [Gradient Descent From Scratch](https://www.youtube.com/watch?v=gsfbWn4Gy5Q) in Python. The scripts employ numpy for mathematical operations and matplotlib for visualizations.

2D Gradient Descent
- The function defines a mathematical function, its derivative, an initial position, and a learning rate. The script iteratively updates the position using the derivative and learning rate, visualizing the optimization process in real-time.

3D Gradient Descent
- The function defines a mathematical function and its gradient in two dimensions. Three positions are initialized, and the script iteratively updates these positions using their respective gradients and a learning rate. The 3D plot showcases the optimization journey.


## Author
Vladimir Balabanov (Grrr1337)

## License
This project is licensed under the MIT License.

