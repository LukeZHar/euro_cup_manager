def display_matches(matches):
    try:
        for match in matches:
            print(f"{match["Date"]}: {match["Team A"]} {match["Score A"]} - {match['Score B']} {match['Team B']}")
    except KeyError as e:
        print(f"Error displaying matches: Missing Key {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def add_match(matches):
    try:
        team_a = input("Enter team A: ")
        team_b = input("Enter team B: ")
        score_a = int(input("Enter score A: "))
        score_b = int(input("Enter score B: "))
        date = input("Enter date (YYYY-MM-DD): ")
        
        match = {
            "Team A": team_a,
            "Team B": team_b,
            "Score A": score_a,
            "Score B": score_b,
            "Date": date
        }
        
        matches.append(match)
        print("Match added successfully.")
    except ValueError as e:
        print(f"Error: Invalid input. Scores must be integers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def total_goals(matches):
    """
    Calculate total goals scored in the matches

    parameters: matches: List of matches

    returns: Total goals scored
    """
    try:
        return sum(match["Score A"] + match["Score B"] for match in matches)
    except KeyError as e:
        print(f"KeyError: {e}") 
        return 0
    except TypeError:
        print("Error calculating total goals")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0
    
def high_scoring_matches(matches, threshold):
    try:
        return [match for match in matches if match['Score A'] + match['Score B'] > threshold]
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return []