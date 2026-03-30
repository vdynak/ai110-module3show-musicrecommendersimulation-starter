"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:
    from recommender import load_songs, recommend_songs


def print_profile_results(profile_name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Print top-k recommendations for a named user profile."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print(f"\n=== {profile_name} ===")
    print(f"Preferences: genre={user_prefs['genre']}, mood={user_prefs['mood']}, energy={user_prefs['energy']}")
    print()

    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]
        print(f"{idx}. {song['title']} by {song['artist']}")
        print(f"   Score  : {score:.2f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"   - {reason}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.85},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.90},
        # Edge cases suggested by system-evaluation prompt style.
        "Edge Case - Conflicting Sad High Energy": {"genre": "ambient", "mood": "sad", "energy": 0.90},
        "Edge Case - Very Low Energy Party Mood": {"genre": "house", "mood": "happy", "energy": 0.10},
    }

    for profile_name, user_prefs in profiles.items():
        print_profile_results(profile_name, user_prefs, songs, k=5)


if __name__ == "__main__":
    main()
