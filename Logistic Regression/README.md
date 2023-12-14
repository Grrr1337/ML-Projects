# Logistic Regression Demo

**Logistic Regression** is a commonly used algorithm for binary classification tasks. In this example, I am displaying on how to perform binary classification using Logistic Regression in Python with the popular scikit-learn library. We'll use a fictional dataset for illustration purposes.

#### Decision Boundary Plot
The "Decision Boundary Plot" visually represents the boundary created by the Logistic Regression model to distinguish between different classes in a binary classification scenario. The decision boundary is a crucial element in understanding how the model classifies data points into one of two classes. In the plot:

- The background colors indicate the regions predicted for each class.
- Data points are scattered based on their actual class, providing a clear view of the separation achieved by the model.

#### Multi-Class Prediction Plot
The "Multi-Class Prediction Plot" illustrates the actual predictions made by the Logistic Regression model on test data in a scenario involving multiple classes. In this plot:

- Each class is represented by distinct markers and colors.
- Data points are scattered based on their predicted class.
- The plot helps assess the model's ability to generalize and correctly classify instances across various classes.

## Screenshots

### Decision Boundary Plot

![Decision Boundary](Decision%20Boundary.jpg)

### Multi-Class Prediction Plot

![Multi-Class Prediction](Multi-Class%20Prediction.jpg)


## Overview

The script includes the following key components:

- Importing necessary libraries
- Generating a random dataset for binary classification
- Splitting the dataset into training and testing sets
- Creating a Logistic Regression model
- Fitting the model to the training data
- Making predictions on the test data
- Evaluating the model's performance using accuracy, confusion matrix, and classification report
- Plotting the decision boundary

## Results

The accuracy, confusion matrix, and classification report are printed to the console for analysis.

## Decision Boundary

The decision boundary is visualized using the `plot_decision_boundary` function, showcasing how the model separates the classes.

## Additional Functionality

In addition to binary classification, the script offers a versatile function for multi-class Logistic Regression. Here's a breakdown of its functionality:

1. Data Generation:
    - The function generates random data with multiple classes using scikit-learn's `make_blobs`.
2. Data Splitting:
    - The generated dataset is split into training and testing sets using `train_test_split` to ensure robust model evaluation.
3. Model Configuration:
    - A Logistic Regression model is created with the `LogisticRegression` class from scikit-learn, configured for multi-class classification using the 'multinomial' option and 'lbfgs' solver.
4. Model Training:
    - The Logistic Regression model is trained on the training data, enabling it to learn the relationships between features and classes.
5. Decision Boundary Visualization:
    - The script visualizes the decision boundary on a scatter plot, showcasing how the model distinguishes between different classes.
6. Prediction Analysis:
    - Actual predictions on the test data are plotted alongside the decision boundary, providing a clear representation of the model's performance.

## Author
Vladimir Balabanov ( **Grrr1337** )

## License
This project is licensed under the MIT License.


