# PredictiveMaintenance-Internship

# Predictive Maintenance System for Turbo Engines

## Overview

The Predictive Maintenance System is designed to predict the remaining useful life (RUL) of turbo engines to anticipate asset state, avoid downtime, and prevent breakdowns. The system uses machine learning algorithms to analyze sensor data from turbofan jet engines and provides real-time RUL predictions.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Objectives](#project-objectives)
3. [Features](#features)
4. [Installation and Setup](#installation-and-setup)
5. [Usage](#usage)
6. [Model Training](#model-training)
7. [Web Dashboard](#web-dashboard)
8. [Monitoring and Maintenance](#monitoring-and-maintenance)
9. [Results and Evaluation](#results-and-evaluation)
10. [Contributing](#contributing)
11. [License](#license)

## Introduction

In the industry, prognostics and health management are key topics for anticipating asset state and avoiding downtime and breakdowns. This project aims to predict the remaining useful life (RUL) of each engine using sensor data and machine learning algorithms.

## Project Objectives

- Train and evaluate machine learning models for RUL prediction.
- Develop a web-based dashboard to visualize engine health and RUL predictions.
- Implement a monitoring system to track the performance of the deployed model.
- Schedule proactive maintenance activities using the predicted RUL.

## Features

- Data preprocessing and feature engineering for model training.
- Model selection and hyperparameter tuning for optimal performance.
- Real-time RUL predictions using a deployed prediction API.
- Web dashboard to visualize engine health and RUL predictions.
- Monitoring system to track model performance.
- Maintenance scheduler to plan proactive maintenance.

## Installation and Setup

1. Clone this repository: `git clone https://github.com/shrutidhange/PredictiveMaintenance-Internship.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Prepare the data and preprocess it using the scripts in the `data_preprocessing` directory.
2. Train the machine learning models using the scripts in the `model_training` directory.
3. Deploy the best-performing model as a real-time prediction API using the deployment script in the `deployment` directory.
4. Launch the web-based dashboard using the command: `python dashboard.py`.
5. Monitor the model's performance using the monitoring script in the `monitoring` directory.

## Model Training

- The `model_training` directory contains scripts to train different machine learning models on the preprocessed data.
- Use hyperparameter tuning techniques like Grid Search or Random Search to optimize model performance.
- Evaluate the models using validation data and choose the best-performing model for deployment.

## Web Dashboard

- The web-based dashboard provides an intuitive interface to visualize engine health and RUL predictions.
- Access the dashboard by running the `dashboard.py` script.
- Interact with the dashboard to explore individual engine details and historical predictions.

## Monitoring and Maintenance

- The monitoring system tracks the deployed model's performance and sends alerts for anomalies or degradation.
- Use the maintenance scheduler to plan proactive maintenance activities based on the predicted RUL.

## Results and Evaluation

- The `results` directory contains evaluation metrics and visualizations of model performance.
- Use the information to assess the accuracy and effectiveness of the predictive maintenance system.

## Contributing

We welcome contributions to improve the project. To contribute, please follow the guidelines in the `CONTRIBUTING.md` file.

## License

This project is licensed under the [MIT License](LICENSE).

