from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]

    def create_body(self):
        """Creating N numbers of snake body"""
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        body = Turtle()
        body.penup()
        body.color('white')
        body.shape('circle')
        body.goto(position)
        self.snake_body.append(body)

    def extend(self):
        """
        Add new segment to the snake \
        while the snake body eat
        """
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)