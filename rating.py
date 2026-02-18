# Movie Preference ML Example - Survey Data
# By: Shassh / CAMS
# This code creates graphs based on survey data

# If you do not have pandas or matplotlib installed you will need to 
# import pandas in Terminal. Open VS Code, open Terminal and type: 
# py -m pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Input your dataset from survey
data = {
    "Movie": [
        "Interstellar", "Avengers Endgame", "Spiderverse: Across the spiderverse", 
        "Spiderverse: Across the spiderverse", "Spiderverse: Across the spiderverse",
        "Avengers Endgame", "Interstellar", "Avengers Endgame", 
        "Spiderverse: Across the spiderverse", "Interstellar",
        "Spiderverse: Across the spiderverse", "Avengers Endgame", "Interstellar",
        "Avengers Endgame", "Interstellar", "Spiderverse: Across the spiderverse",
        "Avengers Endgame", "Spiderverse: Across the spiderverse",
        "Spiderverse: Across the spiderverse", "Avengers Endgame", "Avengers Endgame",
        "Avengers Endgame", "Spiderverse: Across the spiderverse", "Zootopia 2",
        "Zootopia 2"
    ],
    
    "Genre": [
        "Suspense", "Adventure", "Drama", "Action", "Comedy",
        "Action", "Action", "Action", "Suspense", "Horror",
        "Comedy", "Action", "Suspense", "Action", "Action",
        "Action", "Action", "Comedy", "Comedy", "Adventure",
        "Action", "Comedy", "Horror", "Comedy", "Drama"
    ],
    
    "Grade": [
        10, 10, 10, 10, 10,
        10, 11, 11, 12, 10,
        10, 10, 10, 10, 10,
        10, 11, 12, 10, 10,
        10, 10, 10, 10, 10
    ],
    
    "MoviesPerWeek": [
        1, 0, 0, 1, 0,
        2, 1, 1, 3, 0,
        4, 0, 2, 0, 0,
        1, 1, 0, 0, 0,
        2, 3, 1, 1, 2
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display first few rows
print("Movie Preference Dataset (25 Students):")
print(df)
print("\n" + "="*50 + "\n")

# Display summary statistics
print("Summary Statistics:")
print(f"Total responses: {len(df)}")
print(f"\nMost popular movie: {df['Movie'].value_counts().index[0]} ({df['Movie'].value_counts().iloc[0]} votes)")
print(f"Most popular genre: {df['Genre'].value_counts().index[0]} ({df['Genre'].value_counts().iloc[0]} votes)")
print(f"Average movies per week: {df['MoviesPerWeek'].mean():.2f}")
print("\n" + "="*50 + "\n")

# Bar Graph of Genres
# ---------------------------
genre_counts = df["Genre"].value_counts()

plt.figure(figsize=(10, 6))
genre_counts.plot(kind="bar", color="skyblue")
plt.title("Favorite Movie Genres (25 Students)")
plt.xlabel("Genre")
plt.ylabel("Number of Students")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter Plot - Movies Watched vs Grade
# ---------------------------
plt.figure(figsize=(10, 6))
plt.scatter(df["Grade"], df["MoviesPerWeek"], color="green", s=100, alpha=0.6)
plt.xlabel("Grade Level")
plt.ylabel("Movies Watched Per Week")
plt.title("Movies Watched vs Grade Level")
plt.grid(True)
plt.tight_layout()
plt.show()

# Additional Graph - Favorite Movies
# ---------------------------
movie_counts = df["Movie"].value_counts()

plt.figure(figsize=(12, 6))
movie_counts.plot(kind="bar", color="coral")
plt.title("Favorite Movies (25 Students)")
plt.xlabel("Movie")
plt.ylabel("Number of Votes")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()