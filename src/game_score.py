def display_games(games):
    try:
        for score in games:
            print(f"{score['Date']}: {score['Name']} {score['Score']} - {score['Bonus']}")
    except KeyError as e:
        print(f"Error displaying score: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


def add_score(games):
    try:
        name = input("Enter Player name: ")
        score = int(input("Enter Score : "))
        bonus = int(input("Enter Bonus: "))
        date = input("Enter Date (YYY-MM-DD)")

        score = {"Player": name, "Score ": score, "Bonus": bonus, "Date": date}
        games.append(score)
        print("Score successfully added.")
    except ValueError:
        print("Error: Invalid input. Scores must be in integers.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


def high_scoring_game(score, threshold):
    try:
        return [score for score in score if score['Score'] > threshold]
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return []