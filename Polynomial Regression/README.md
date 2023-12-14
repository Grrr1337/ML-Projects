# Polynomial Regression

**Polynomial Regression** is an extension of linear regression that allows for the modeling of non-linear relationships between variables. It achieves this by introducing polynomial features, enabling the algorithm to fit a polynomial equation to the data. The primary purpose of Polynomial Regression is to capture more complex patterns in the data compared to traditional linear regression.


This is a **demonstration** of my exploration regarding the use of Polynomial Regression.


#### Key Features
- **Polynomial Features**: Polynomial Regression introduces higher-degree polynomial features to the input data, enabling the model to capture and represent non-linear relationships between variables.

- **Degree**: The degree of the polynomial determines the complexity of the model. A higher degree allows the model to fit more complex patterns in the data. However, selecting a very high degree ``may lead to overfitting``, where the model performs well on the training data but poorly on new, unseen data.

- **Linear Regression Basis**: Despite its name, **Polynomial Regression utilizes a linear regression model**. The linearity refers to the linearity in the coefficients of the features, meaning that the model is linear with respect to its parameters, even though the relationship between the features and the target variable is non-linear.

- **Model Flexibility**: Polynomial Regression is a flexible modeling approach that can adapt to various types of data, making it suitable for scenarios where the relationship between variables is non-linear. So that means that it is capturing a wide range of relationships between variables. 

## Screenshot
![Polynomial Regression](Polynomial%20Regression.bmp)


## Overview
My python script demonstrates the application of Polynomial Regression using the scikit-learn library. Two functions are defined:

- Linear Regression
    - While a Linear Regression function illustrates a simple linear regression scenario, fitting a line to randomly generated data points, It serves as a baseline for comparison with Polynomial Regression.

- Polynomial Regression
    - The Polynomial Regression function showcases Polynomial Regression by generating random data with a cubic relationship. It applies a fourth-degree polynomial transformation to the features, allowing the linear regression model to capture the non-linear pattern.

## Usage
The degree of the polynomial features is adjusted in the `PolynomialFeatures` class to control the complexity of the model. Experiment with different noise factors and degrees to observe the impact on the model's ability to capture underlying patterns.

For a visual representation of the results, the script generates scatter plots of the data points along with the fitted regression lines.

## Author
Vladimir Balabanov ( **Grrr1337** )

## License
This project is licensed under the MIT License.


