# StockPredictionServices

This project is a RESTful API using Flask with Endpoints that:

* Predict Stock value for a given date.
* Predict Stock prices for given list of dates.

## Dataset

The model is tained with one year data of Apple Inc stock prices taken from NASDAQ. The data can be downloaded from [here](https://www.nasdaq.com/symbol/aapl/historical).

## Model
Linear Regression is used to train the model. [This tutorial explains Linear Regression model with Scikit](https://ruthwik.github.io/machinelearning/2018-04-06-linear-regression-scikit/).

## Prerequisites
* Python 3
* Flask
* Sklearn
* Pandas
* Pycharm
* Postman

## How to build this project

1. Download the project.
2. Import the project into Pycharm
3. Run the main.py. 

> Flask generally uses port 5000

### End points

 1. Import the StockPrediction.postman_collection.json into the Postman.
 2. Go to body of "Predict stock value for a date". Change the date and send the request.
    The sample reponse would be
    ```
    {
    "price": 177.067266992859
    }
    ```
  3. Go to body of "Predict stock prices for list of dates ". Give list of dates and send the request.
     The sample response would be
     
     ```
     
     {
    "stock": [
        {
            "price": 178.5367858460645
        },
        {
            "price": 177.55710661059402
        },
        {
            "price": 179.90833677572323
        },
        {
            "price": 176.67539529867076
        }
    ]
  }
  
    ```
