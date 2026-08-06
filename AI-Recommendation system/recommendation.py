import pandas as pd
import difflib

# Load dataset
data = pd.read_csv("dataset/recommendations.csv")

print("=" * 50)
print("        AI RECOMMENDATION SYSTEM")
print("=" * 50)

# Get user input
user_interest = input("Enter your interest/category: ").strip()

# Get unique categories
categories = data["Category"].unique().tolist()

# Find closest matching category
match = difflib.get_close_matches(user_interest, categories, n=1, cutoff=0.4)

if match:
    selected_category = match[0]

    print("\nYou entered:", user_interest)
    print("Matched Category:", selected_category)
    print("\nRecommended Items:\n")

    recommendations = data[data["Category"] == selected_category]

    for i, item in enumerate(recommendations["Item"], start=1):
        print(f"{i}. {item}")

else:
    print("\nSorry! No matching category found.")
    print("\nAvailable Categories are:")
    for category in categories:
        print("-", category)

print("\nThank you for using AI Recommendation System!")
