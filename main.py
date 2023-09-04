def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20
    else:
        return False

def rackets_cost(racket_brand):
    if rackets_brand == "bullpadel":
        return 100
    elif racket_brand == "nox":
        return 140
    elif racket_brand == "siux": 
        return 200

def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5

def padel_game_cost():
    court_type = (input("Enter the court type:"))
    rackets_cost = (input("Enter racket brand:"))
    ball_boxes = int(input("1 / 2 / 3 ?"))
    result = ("padel_court_cost (court_type) + padel_balls_cost (ball_boxes) + rackets_cost (rackets_brand)" )
    return result

print(padel_game_cost()) 