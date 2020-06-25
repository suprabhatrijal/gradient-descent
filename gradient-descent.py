import matplotlib.pyplot as plt

#li is the list of points to do linear regression on
li= [(8,3),(18,10),(11,4),(13,6),(14,8),(22,12),(12,5),(9,4),(20,9),(25,14)]
#m a random slope, it way be any value
m = 1
# c is a random intercept, it maybe any value
c = 500
#learning_rate is the learning rate
learning_rate = 0.0001


#simple function that takes data(points) to be predicted, slope and intercept of the model to give the predicted value
def predict(points, slope, intercept):
    predict_list = []
    for point in points:
        x = point[0]
        y_predict = slope*x + intercept
        predict_list.append(y_predict)
    return predict_list

#Gives the RSS of the points and the prediction
def rss(points, prediction):
    rss = 0
    for i in range(0, len(prediction)):
        x = points[i][0]
        y = points[i][1]
        y_predict = prediction[i]

        rss += (y-y_predict)**2
    return rss

#finds the derivative of the RSS w.r.t. slope and intercept
def rss_derivative(points,slope, intercept):
    d_slope = 0
    d_intercept = 0
    for point in points:
        x = point[0]
        y = point[1]
        d_slope += 2*-x*(y-(slope*x+intercept))
        d_intercept += -2*(y-(slope*x+intercept))

    return  {'slope':d_slope, 'intercept':d_intercept}

#dictionary of derivatives of RSS w.r.t. slope and intercept 
derivatives = rss_derivative(li,m,c)


print("RSS before regression: ", rss(li, predict(li,m,c)))

#algorithm
while abs(derivatives['slope']) >= 0.001 or abs(derivatives['intercept']) >= 0.001:
    step_slope = derivatives['slope'] * learning_rate
    step_intercept = derivatives['intercept'] * learning_rate
    m -= step_slope
    c -= step_intercept

    derivatives = rss_derivative(li, m, c)



print("Slope: ",m, "Intercept: ",c)
print("RSS after regression: ", rss(li, predict(li,m,c)))


#Matplotlib to display the graph
xs = [x[0] for x in li]
ys = [x[1] for x in li]

x =  [x[0] for x in li]
y =[m*x + c for x in x]

plt.scatter(xs,ys)
plt.plot(x,y)

plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.margins(x=0.14,y=0.14)
for i_x, i_y in zip(xs, ys):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

plt.show()

