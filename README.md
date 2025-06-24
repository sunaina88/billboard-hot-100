# 🎧 Billboard to Spotify Playlist Generator

> Give a date. Get a playlist.

This Python script scrapes the Billboard Hot 100 chart for a given date and automatically creates a **public Spotify playlist** with those songs using the Spotify Web API.

---

## 🚀 Features

- Scrapes Billboard Hot 100 using BeautifulSoup
- Authenticates securely using Spotify OAuth 2.0
- Searches Spotify for matching songs by name and year
- Creates a public playlist in your Spotify account

---

## 🛠️ Setup Instructions

Follow these steps to run the project on your machine:

### 1. Clone the Repository

```bash
git clone https://github.com/sunaina88/billboard-hot-100.git
cd billboard-hot-100
```

### 2. Create a `.env` File

In the project folder, create a file named `.env` and paste your Spotify credentials:

```env
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
```

### 3. Install Dependencies

Make sure you're in your project folder, then run:

```bash
pip install -r requirements.txt
```

### 4. Run the Script

To start the program, run:

```bash
python main.py
```
You'll be prompted to enter a date in the format:
YYYY-MM-DD

## 📸 Example Output

```bash
Which year would you like to travel to? Type the date in this format YYYY-MM-DD:
2024-08-08
```

```bash
Here is your new playlist: "https://open.spotify.com/playlist/3YIHc2uSGHYoY3jPKF4NLv?si=f77f97a91cb042d7"
```
A link to your new Spotify playlist will be generated as output and you can find your new playlist with the Billboard Hot 100 songs of that date in your Spotify playlists folder.

## 🙋‍♀️ Author

**sunaina ☀**  (she/her)

GitHub: [@sunaina88](https://github.com/sunaina88)

---

Feel free to ⭐ the repo if you found it useful or fun!
