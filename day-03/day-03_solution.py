import requests
import json

API_URL = "https://ghibliapi.vercel.app/films"

def fetch_movies():
    response = requests.get(API_URL)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch movies")
        return []
def process_movies(movies):
    processed = []

    for movie in movies:
        processed.append({
            "title": movie["title"],
            "director": movie["director"],
            "release_year": movie["release_date"],
            "rating": movie["rt_score"]
        })
    return processed

def save_to_json(data, filename="movies.json"):
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"\nMovies saved to {filename}")

def main():
    print("Fetching movies from API...")
    movies = fetch_movies()

    print(f"Total movies fetched: {len(movies)}\n")
    processed_movies = process_movies(movies)

    print("Sample Movies:\n")

    for movie in processed_movies[:5]:
        print(f"Title       : {movie['title']}")
        print(f"Director    : {movie['director']}")
        print(f"Year        : {movie['release_year']}")
        print(f"IMDB Score  : {movie['rating']}\n")
        print(f"-" * 35)
    save_to_json(processed_movies)

if __name__ == "__main__":
    main()
