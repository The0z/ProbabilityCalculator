import copy
import random


class Hat:
    def __init__(self, **balls):
        # Obtain keys and put in list
        ballColors = list(balls.keys())
        numBalls = list()
        sum = 0
        # Obtain color of each ball
        for i in ballColors:
            numBalls.append(balls.get(i))
            sum += int(balls.get(i))
        # Creating content instance list
        self.contents = list()
        for i in range(len(ballColors)):
            for j in range(numBalls[i]):
                self.contents.append(ballColors[i])

    def draw(self, drawNum):
        pickedBalls = list()
        if drawNum > len(self.contents):
            drawNum = len(self.contents)   # confg to show order of balls
        for i in range(drawNum):
            index = random.randint(0, len(self.contents)-1)
            pickedBalls.append(self.contents.pop(index))
        return pickedBalls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    occur = 0

    for count in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        balls = dict()

        # Consolidating List into Dictionary
        for ball in hatCopy.draw(num_balls_drawn):
            balls[ball] = balls.get(ball, 0) + 1

        for i in expected_balls.keys():
            if balls.get(i, 0) >= expected_balls.get(i):
                yesMatch = True
            else:
                yesMatch = False
                break
        if yesMatch:
            occur += 1

    return occur/num_experiments
