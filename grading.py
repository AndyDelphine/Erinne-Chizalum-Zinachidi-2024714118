marks = int(input("Enter your Scores(0-100): "))

if marks >= 70:
    print("Grade: A Excellent!")
elif marks >= 60:
    print("Grade: B Good Job")
elif marks >= 50:
    print("Grade: C Good")
elif marks >= 45:
    print("Grade: D Fair")
elif marks >= 40:
    print("Grade: E Fair Effort")
else:
    print("Grade: F Try Harder")


input("Press Enter to exit...")
