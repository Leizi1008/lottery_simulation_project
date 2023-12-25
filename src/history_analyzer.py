import csv

def analyze_history(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        history_data = [row for row in reader]
    # Implement your analysis logic here
    # For example, counting the frequency of each number
    frequency = {'red': {}, 'blue': {}}
    for draw in history_data:
        red_balls = draw[0].split('-')
        blue_balls = draw[1].split('-')
        for ball in red_balls:
            frequency['red'][ball] = frequency['red'].get(ball, 0) + 1
        for ball in blue_balls:
            frequency['blue'][ball] = frequency['blue'].get(ball, 0) + 1
    return frequency
