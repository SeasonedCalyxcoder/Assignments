#Defining a function for greeting the student
def greet(name: str) -> str:
    return f"Hello, {name}! Let's check your performance."

#Function to calculate average score from list of scores
def compute_average(scores: list[int]) -> float:
    return sum(scores) / len(scores) if scores else 0.0

#Function to determine if student has passed based on their average
def has_passed(average: float) -> bool:
    return average >= 50 #Passing mark is 50

#Function that collects student data, computes performance and prints the report
def students_performance() -> None:
    #Prompts the student to enter their name
    name: str = input("Enter student name: ")
    print(greet(name)) #Greets the student

    scores: list[int] = [] #Initializing an empty list to store scores

#Loop to collect scores for 3 subjects
    for i in range(3):
        while True: #Prompts user until a valid score is entered
             try:
                 #Prompt user to enter a score for the current subject
                score = int(input(f"Enter score for subject {i + 1}: "))
                if 0 <= score <= 100: #Range of scores
                    scores.append(score)#Add a valid score to list
                    break#Exit loop
                else:
                    print("Score must be between 0 and 100.") #Invalid range
             except ValueError:
                print("Please enter a valid number.") #Invalid input

    #Compute average score from entered scores
    average_score: float = compute_average(scores)
    #Determine whether the student has passed or failed
    is_pass: bool = has_passed(average_score)

    #Print the report card
    print("\n---- Report Card ----")
    print(f"Name            : {name}")
    print(f"Scores          : {scores}")
    print(f"Average         : {average_score:.2f}")
    print(f"Status          : {'Pass' if is_pass else 'Fail'}")

    assignments_done: int = 5 #Number of completed assignments
    pts: float = 2.5 #Bonus points awarded for the assignments
    total_score: float = average_score + pts #Final score + bonus

    #Print bonus points and final score
    print(f"Bonus Pts       : +{pts} for {assignments_done} assignments")
    print(f"Final Score     : {total_score:.2f}")

#Entry point: runs the program if executed directly
if __name__ == "__main__":
    students_performance()