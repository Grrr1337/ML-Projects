# OPTICS Clustering Interactive Exploration
This Python script provides an interactive exploration of the OPTICS (Ordering Points To Identify the Clustering Structure) clustering algorithm. The code allows the user to *manipulate* the `xi_value` interactively using the `'+'` and `'-'` keys. Additionally, you can cycle through *multiple pre-generated point datasets* by pressing `'P'` (previous) and `'N'` (next).

## Demo
![OPTICS XI Demo](OPTICS%20XI%20Demo.gif)

## Getting Started
1. Dependencies:

One must ensure that have the necessary dependencies installed using:
```bash
pip install numpy pandas matplotlib scikit-learn
```

2. Run the Script:

Execute the script in your Python environment:
```bash
python script.py
```

## Interactive Features
- Adjust xi_value:
    - Press the '+' key to increase the `xi_value`.
    - Press the '-' key to decrease the `xi_value`.
- Switch Between Datasets:
    - Press 'N' for the next pre-generated dataset.
    - Press 'P' for the previous pre-generated dataset.

## Code Structure
- The script utilizes the **OPTICS clustering** algorithm from scikit-learn to cluster 2D point datasets.
- Interactive manipulation of the `xi_value` allows exploration of the algorithm's sensitivity to this parameter.
- The code includes functions to find the optimal `eps` value and perform **OPTICS clustering** on a given dataset.
- Visualization is achieved using matplotlib, providing real-time updates as the `xi_value` is adjusted.

## Exploring OPTICS Clustering
- The script visualizes clusters with different colors and identifies noise points.
- The title dynamically displays key parameters, such as `min_samples`, `xi_value`, and the number of clusters.

## Note
- This script is designed for educational purposes to understand OPTICS clustering behavior with interactive exploration.
- Pre-generated datasets in CSV format are used for quick experimentation.

One is free to explore the interactive features, adjust the `xi_value`, and switch between datasets to observe the impact on OPTICS clustering. 


## Author
Vladimir Balabanov ( **Grrr1337** )

## License
This project is licensed under the MIT License.


