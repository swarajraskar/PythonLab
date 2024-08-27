import math
def ball_collide(ball1, ball2):
    
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    radius_sum = r1 + r2
    
    return distance <= radius_sum


ball_a = (0, 0, 5)  
ball_b = (3, 4, 5)  

is_colliding = ball_collide(ball_a, ball_b)
print("Are the balls colliding?", is_colliding)  