import random


def single_trial(num_people):
    """Simulate a single trial for 'num_people' in the room."""
    days = [False] * 365  # 365 days, initialized to False (no birthday marked)
    for _ in range(num_people):
        birthday = random.randint(0, 364)  # Random birthday from 0 to 364
        if days[birthday]:  # If birthday is already taken
            return True  # Birthday collision detected
        days[birthday] = True  # Mark this birthday as taken
    return False  # No collision detected


def multiple_trials(num_people, num_trials):
    """Run 'num_trials' trials for 'num_people' in the room and return success count."""
    success_count = sum(single_trial(num_people) for _ in range(num_trials))
    return success_count


def prompt_for_threshold():
    """Prompt user for a valid threshold percentage."""
    while True:
        try:
            threshold = int(input("What threshold would you like? (enter as a percent) "))
            if 0 <= threshold <= 100:
                return threshold
            else:
                print("Error: Not a valid percent. Please enter a value between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def prompt_for_trial_count():
    """Prompt user for the number of trials to perform."""
    while True:
        try:
            trials = int(input("Enter the number of trials to perform (e.g., 100000 for accurate results): "))
            if trials > 0:
                return trials
            else:
                print("Error: Number of trials should be greater than zero.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def main():
    # Get user inputs
    threshold = prompt_for_threshold()
    num_trials = prompt_for_trial_count()

    num_people = 2  # Start with 2 people in the room

    while True:
        # Perform the trials and calculate probability
        success_count = multiple_trials(num_people, num_trials)
        probability = (success_count / num_trials) * 100

        # Display the results for the current room size
        print(
            f"For {num_people} people, the probability of a shared birthday was  {success_count} / {num_trials} or {probability:.2f}%")

        # Check if the probability meets or exceeds the threshold
        if probability >= threshold:
            print(
                f"\nTo achieve at least {threshold}% probability of a collision, need {num_people} people in the room.")
            break

        # Increase the room size for the next iteration
        num_people += 1


# Run the improved program
main()