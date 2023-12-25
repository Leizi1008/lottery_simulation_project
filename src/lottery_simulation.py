import random

def simulate_lottery(draws=10000, red_ball_count=35, blue_ball_count=12, red_ball_draw=5, blue_ball_draw=2):
    results = []
    for _ in range(draws):
        red_balls_drawn = sorted(random.sample(range(1, red_ball_count + 1), red_ball_draw))
        blue_balls_drawn = sorted(random.sample(range(1, blue_ball_count + 1), blue_ball_draw))
        results.append({'red': red_balls_drawn, 'blue': blue_balls_drawn})
    return results
