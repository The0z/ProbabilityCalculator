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
        self.content = list()
        for i in range(len(ballColors)):
            for j in range(numBalls[i]):
                self.content.append(ballColors[i])

    def draw(self, drawNum):
        pickedBalls = list()
        if drawNum > len(self.content):
            drawNum = len(self.content)   # confg to show order of balls
        for i in range(drawNum):
            index = random.randint(0, len(self.content)-1)
            pickedBalls.append(self.content.pop(index))
        return pickedBalls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return 0
