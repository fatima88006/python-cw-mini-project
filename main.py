def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20

def rackets_cost(racket_brand):
    if racket_brand == "bullpadel":
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
    court_type = (input("Enter the court type: indoor \ outdoor\n"))
    racket_brand = (input("Enter racket brand: bullpadel \ nox \ siux \n"))
    ball_boxes = int(input("Enter the number of the balls 1 / 2 / 3 \n?"))
    cost = padel_court_cost(court_type) + rackets_cost(racket_brand) + padel_balls_cost(ball_boxes)
    return cost

print (padel_game_cost())  