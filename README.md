# GeoForecastComp

<h1>Model</h1>

In /basicNerualNetapproach you'll find a construction of a nerual network with documented python code.

I used a genetic algorthim to adjust the weights in the training phase of the model. At the momment 50*50=2500 mututations are created, and a single best one is selected for redefinition of each layer's weights as the function back propagates.

![unnamed](https://github.com/user-attachments/assets/42cf8072-9837-44f9-85a3-1f76073a9067)

<h1>App</h1>

The app is currently being developed. Currently the backend is written in python with FastAPI with a single graphql end point, as well as a post request endpoint. The front end is currently a simple react app for querying these end points with the inserted text being the payload. The plan is the have open ai automatically generate model inputs that satisfy the geology count for each of the 300 inputs that are available in an easy to approach way. After this is completed I'll have some error analysis for the model dispalyed through graphs with respect to the training data.
