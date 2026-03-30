# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Goal / Task  

This model suggests songs from a small catalog.
It predicts which songs best match a user vibe.
The vibe is based on genre, mood, and energy target.

---

## 3. Data Used  

The dataset has 18 songs.
Each song has genre, mood, energy, tempo, valence, danceability, and acousticness.
I expanded the starter set to include more genres and moods.
The main limit is size. There are still very few songs per genre.

---

## 4. Algorithm Summary  

For each song, the model gives points.
It adds points for genre match and mood match.
It also adds energy similarity points based on how close song energy is to user energy.
Then it sorts songs by total score and returns the top 5.

---

## 5. Observed Behavior / Biases  

The model is very sensitive to energy.
This can create an energy filter bubble.
Songs with close energy can rank high even when mood feels wrong.
Another issue is that `likes_acoustic` is not used in scoring yet.

---

## 6. Limitations and Bias 

The catalog is small, so many user tastes are underrepresented.
Exact mood matching is strict and misses near moods.
The model does not use history, skips, likes, or context.
Because of that, it can feel repetitive and narrow.

---

## 7. Evaluation  

I tested High-Energy Pop, Chill Lofi, and Deep Intense Rock.
I also tested edge cases with conflicting mood and energy.
I compared top 5 results and checked if they felt right.
One surprise: "Gym Hero" often appeared for Happy Pop users.
This happens because energy closeness can outweigh mood differences.

---

## 8. Intended Use and Non-Intended Use  

Intended use: classroom simulation and learning recommender basics.
Intended use: quick CLI demos of scoring and ranking behavior.
Non-intended use: real music platform decisions.
Non-intended use: any high-stakes personalization, fairness, or business decisions.

---

## 9. Ideas for Improvement  

Add acousticness preference into scoring.
Use softer mood similarity instead of exact mood match only.
Add diversity rules so top 5 is not always the same style.

---

## 10. Personal Reflection

My biggest learning moment was seeing how one weight change can completely change the top recommendation for edge-case users. AI tools helped me move faster when writing prompts, generating test profiles, and formatting outputs, but I still had to double-check the math and ranking behavior by running the program myself. I was surprised that a simple rule-based scorer could still feel like a real recommender when the output included clear reasons and matched a vibe like high-energy pop. I would extend this project by using acousticness in scoring, adding softer mood matching, and testing a diversity rule so the top results are less repetitive.
