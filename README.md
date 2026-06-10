# Daily Affirmations

Daily Affirmations is a very small Streamlit app. It displays one positive message at a time from `data/affirmations.txt`.

## How to Run Locally

1. Install the dependency:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

3. Open the local URL shown in the terminal. It is usually `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push this project to GitHub.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Create a new app from the repository.
4. Set the main file path to `app.py`.

No database, backend server, Docker setup, or extra framework is required.

## Requirements

- Python 3.11 or newer
- Streamlit

## Project Structure

```txt
.
├── app.py
├── assets/
│   └── thumbs_up.jpeg
├── data/
│   └── affirmations.txt
└── requirements.txt
```
