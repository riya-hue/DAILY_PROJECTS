def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"

def main():
    print("===== Student Grade Calculator =====")

    subjects = ["Maths", "Science", "English", "History", "Computer"]
    marks = []

    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("❌ Please enter a valid number between 0 and 100.")
            except ValueError:
                print("❌ Invalid input! Please enter a numeric value.")

    total = sum(marks)
    percentage = total / len(subjects)

    grade = calculate_grade(percentage)

    print("\n===== RESULT =====")
    print(f"Total Marks: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade:", {grade})
    print("=====================")

if __name__ == "__main__":
    main()
