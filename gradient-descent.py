import matplotlib.pyplot as plt

li= [(8,3),(18,10),(11,4),(13,6),(14,8),(22,12),(12,5),(9,4),(20,9),(25,14)]
m = 1
c = 500
learning_rate = 0.0001



def predict(points, slope, intercept):
    predict_list = []
    for point in points:
        x = point[0]
        y_predict = slope*x + intercept
        predict_list.append(y_predict)
    return predict_list


def RSS(points, prediction):
    rss = 0
    for i in range(0, len(prediction)):
        x = points[i][0]
        y = points[i][1]
        y_predict = prediction[i]

        rss += (y-y_predict)**2
    return rss


def RSS_derivative(points,slope, intercept):
    d_slope = 0
    d_intercept = 0
    for point in points:
        x = point[0]
        y = point[1]
        d_slope += 2*-x*(y-(slope*x+intercept))
        d_intercept += -2*(y-(slope*x+intercept))

    return  {'slope':d_slope, 'intercept':d_intercept}

derivatives = RSS_derivative(li,m,c)
step_count = 0
print("RSS before regression: ", RSS(li, predict(li,m,c)))
while abs(derivatives['slope']) >= 0.001 or abs(derivatives['intercept']) >= 0.001:
    step_slope = derivatives['slope'] * learning_rate
    step_intercept = derivatives['intercept'] * learning_rate
    m -= step_slope
    c -= step_intercept

    derivatives = RSS_derivative(li, m, c)


    step_count += 1
print("Slope: ",m, "Intercept: ",c)

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

print("RSS after regression: ", RSS(li, predict(li,m,c)))
