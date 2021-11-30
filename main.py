
# The cmu_112_graphics file is from https://www.cs.cmu.edu/~112/notes/notes-graphics.html and credited to
# Carnegie Mellon University
from cmu_112_graphics import *
import random


def step(app):
    new_center = app.center
    shortest_length, furthest = compute_longest(app, app.center)
    for dx in [-3, 0, 3]:
        for dy in [-3, 0, 3]:
            if dx == dy == 0:
                continue
            center = (app.center[0] + dx, app.center[1] + dy)
            length, furthest = compute_longest(app, center)
            if length < shortest_length:
                shortest_length = length
                new_center = center

    if app.center == new_center:
        app.over = True
    else:
        app.longest_len = shortest_length
        app.furthest_point = furthest
        app.center = new_center


def reset_points(app, num):
    app.points = []
    for _ in range(num):
        app.points = app.points + [(random.randint(int(app.width) // 4, int(app.width)) * 3 // 4,
                                    random.randint(int(app.height) // 4, int(app.height) * 3 // 4))]


def distance(x0, y0, x1, y1):
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** (1 / 2)


def compute_longest(app, center):
    longest = 0
    furthest = app.points[0]

    for point in app.points:
        dist = distance(point[0], point[1], center[0], center[1])
        if dist > longest:
            longest = dist
            furthest = point

    return longest, furthest


def timerFired(app):
    if app.over:
        return

    app.timer += app.timerDelay

    if app.timer > 50:
        step(app)
        app.timer = 0


def keyPressed(app, event):
    if event.key == "r" and app.over:
        appStarted(app)


def appStarted(app):
    app.points = []
    reset_points(app, 10)
    app.center = (500, 400)
    app.longest_len, app.furthest_point = compute_longest(app, app.center)
    app.over = False
    app.timer = 0


def redrawAll(app, canvas):
    canvas.create_oval(app.center[0] - app.longest_len - 4, app.center[1] - app.longest_len - 4,
                       app.center[0] + app.longest_len + 4, app.center[1] + app.longest_len + 4,
                       fill="blue")

    canvas.create_oval(app.center[0] - 4, app.center[1] - 4,
                       app.center[0] + 4, app.center[1] + 4, fill="orange", width=0)

    for point in app.points:
        canvas.create_oval(point[0] - 4, point[1] - 4, point[0] + 4, point[1] + 4, fill="black", width=0)

    canvas.create_line(app.furthest_point[0], app.furthest_point[1],
                       app.center[0], app.center[1])


if __name__ == '__main__':
    runApp(width="1000", height="800")
