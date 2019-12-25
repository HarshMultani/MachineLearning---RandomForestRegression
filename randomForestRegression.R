# Random Forest Regression

# Install the packages
install.packages("randomForest")
library(randomForest)
install.packages("ggplot2")
library(ggplot2)

# Import the dataset
dataset <- read.csv('Position_Salaries.csv')


# Fit the Random Forest Model
set.seed(1234)
# model <- randomForest(Salary ~ Level, data = dataset, ntree = 10)
model <- randomForest(x = dataset[2], y = dataset$Salary, ntree = 100)


# Predicting the results
YPred <- predict(model, data.frame(Level = 6.5))


# Visualise the result in higher dimensions
xGrid <- seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') + geom_line(aes(x = xGrid, y = predict(model, newdata = data.frame(Level = xGrid))), colour = 'blue') + ggtitle('Random Forest Visualisation') + xlab('Level') + ylab('Salary')
