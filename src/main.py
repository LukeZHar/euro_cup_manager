from file_operations import load_matches, save_matches
from match_operations import display_matches, add_match, total_goals, high_scoring_matches

FILE_PATH = '../data/matches.json'

def main():
    matches = load_matches(FILE_PATH)
    
    if not matches:
        print('No matches loaded or an error occured. Exiting...')
        return
    while True:
        print('\nEuro Cup Manager:')
        print('1. Display all matches')
        print('2. Add a new match')
        print('3. Display total goals scored')
        print('4. Display high scoring matches')
        print('5. Save and Exit')

        choice = input('Choose an option: ')

        if choice == '1':
            display_matches(matches)
        elif choice == '2':
            add_match(matches)
        elif choice == '3':
            print(f"Total goals scored: {total_goals(matches)}")
        elif choice == '4':
            high_scoring = high_scoring_matches(matches)
            display_matches(high_scoring)
        elif choice == '5':
            try:
                save_matches(matches, FILE_PATH)
                break
            except Exception as e:
                print(f'Error saving matches: {e}')        
        else:
            print('Invalid choice. Please try again')

if __name__ == '__main__':
    main()