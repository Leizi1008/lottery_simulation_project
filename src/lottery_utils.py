import csv

def save_results_to_csv(results, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Red Balls', 'Blue Balls']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow({'Red Balls': '-'.join(map(str, result['red'])), 'Blue Balls': '-'.join(map(str, result['blue']))})

def save_results_to_txt(results, filename):
    with open(filename, 'w') as txtfile:
        for result in results:
            txtfile.write(f"Red Balls: {'-'.join(map(str, result['red']))} | Blue Balls: {'-'.join(map(str, result['blue']))}\n")
