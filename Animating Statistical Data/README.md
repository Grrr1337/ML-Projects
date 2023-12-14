# Animating Statistical Data

**Enhance Data Understanding Through Animation**

Animating statistical data plays a crucial role in presenting information to end users. Dynamic visualizations bring data to life, providing a more engaging and intuitive understanding of complex trends, changes, and patterns. This project showcases the power of animation in making statistical insights accessible and actionable.

## Overview
This project showcases the animation of statistical data using Python. The code demonstrates two examples:

1. **Web Browser Market Share Animation**
    - Visualizes the market shares of different web browsers over the years.
2. **GDP Per Capita Animation**
    - Illustrates the GDP per capita for some of the poorest balkan countries *(esp. Bulgaria)* over a span of several years.

## Demo
*NOTE: My `gif recorder` may have `ruined the colors` a bit.*

![Animating Statistical Data](Animating%20Statistical%20Data.gif)

## Code Contents
1. **Web Browser Market Share Animation** ( 1st function ):
    - The labels array represents the browser names.
    - The shares array contains the market shares for each browser over different years.
    - Adjust the years and shares as needed.
    - Run the script to visualize the animated bar chart.
2. **GDP Per Capita Animation** ( 2nd function ):
    - Reads GDP data from a CSV file.
    - Selects specific countries and animates their GDP per capita over the available years.
    - The resulting bar chart dynamically updates to reflect changes in GDP over time.

## Additional Notes
- The code employs the **matplotlib** library for creating animated visualizations.
- For the GDP animation, random colors are generated for each country, providing a visually appealing and distinctive display.

## Requirements
- Python 3.x
- numpy
- matplotlib
- pandas

## Acknowledgments
This project was inspired by the desire to create engaging visualizations of statistical data, providing insights into trends and changes over time.
[Link to the Video Tutorial](https://www.youtube.com/watch?v=IEQhZIv1Cq0)

## Author
Vladimir Balabanov (Grrr1337)

## License
This project is licensed under the MIT License.


