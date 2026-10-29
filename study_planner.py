# MY AI STUDY PLANNER
# A beginner-friendly Python program for creating a personalized study plan.

print("================================")
print("      MY AI STUDY PLANNER")
print("================================")

student_name = input("Enter your name: ").strip()
learning_goal = input("What is your AI learning goal? ").strip()

# Keep asking until the student enters a valid number of days.
while True:
    try:
        study_days = int(input("How many days per week will you study (1-7)? "))
        if 1 <= study_days <= 7:
            break
        print("Please enter a number from 1 to 7.")
    except ValueError:
        print("Please enter a whole number.")

# Keep asking until the student enters a valid number of daily hours.
while True:
    try:
        daily_hours = float(input("How many hours will you study each study day? "))
        if daily_hours > 0:
            break
        print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number, such as 1 or 1.5.")

weekly_hours = study_days * daily_hours

# A simple, flexible study routine.
study_activities = [
    "Learn a new concept and take notes",
    "Watch a lesson or read a beginner tutorial",
    "Practice with a small Python or AI-related exercise",
    "Review previous notes and summarize what you learned",
    "Work on a small project or practical example",
    "Revise difficult topics and practice problem-solving",
    "Review your progress and plan the next week"
]

plan_lines = [
    "================================",
    "       MY AI STUDY PLANNER",
    "================================",
    f"Student name: {student_name}",
    f"AI learning goal: {learning_goal}",
    f"Study days per week: {study_days}",
    f"Daily study hours: {daily_hours:g}",
    f"Total weekly study hours: {weekly_hours:g}",
    "",
    "PERSONALIZED STUDY PLAN",
    "-----------------------",
]

for day in range(study_days):
    activity = study_activities[day]
    plan_lines.append(
        f"Day {day + 1}: {activity} ({daily_hours:g} hour(s))"
    )

plan_lines.extend([
    "",
    "Helpful tips:",
    "- Take short breaks during longer study sessions.",
    "- Practice regularly instead of only reading.",
    "- Adjust the activities to match your learning goal.",
    "- Review your progress at the end of each week.",
    "",
    "Good luck with your AI learning journey!"
])

study_plan = "\n".join(plan_lines)

print("\n" + study_plan)

try:
    with open("study_plan.txt", "w", encoding="utf-8") as file:
        file.write(study_plan)
    print("\nYour study plan has been saved to study_plan.txt")
except OSError:
    print("\nSorry, the study plan could not be saved. Check folder permissions.")
