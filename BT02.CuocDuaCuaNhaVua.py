n = int(input())
x, y = map(int,input().split())
x_white = 1
y_white = 1
step_white_x = x - x_white
step_white_y = y - y_white
step_black_x = n - x
step_black_y = n - y
if step_white_x > step_white_y:
    step_white = step_white_x
else:
    step_white = step_white_y
if step_black_x > step_black_y:
    step_black = step_black_x
else:
    step_black = step_black_y
if step_white == step_black:
    print("White")
elif step_white < step_black:
    print("White")
else:
    print("Black")