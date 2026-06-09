# 🇮🇳 India Census Data Visualization

An interactive map-based dashboard built with Streamlit and Plotly that visualizes **India Census 2011** data at the district level.

🔗 **Live App:** [k6zpk7ttllgaojegkzq4xz.streamlit.app](https://k6zpk7ttllgaojegkzq4xz.streamlit.app/)

---

## 📊 What It Does

- Plots every district of India on an interactive map
- **Bubble size** represents a primary parameter (e.g. Population)
- **Bubble color** represents a secondary parameter (e.g. Literacy Rate)
- Filter by state or view all of India at once
- Hover over any district to see its name and data

---

## 🗂️ Dataset

India Census 2011 — district-level data with the following columns:

| Column | Description |
|---|---|
| State | State name |
| District | District name |
| Latitude / Longitude | Geographic coordinates |
| Population | Total population |
| Male / Female | Male and female population |
| Literate | Number of literate people |
| Households_with_Internet | Internet-connected households |
| Housholds_with_Electric_Lighting | Households with electricity |
| sex_ratio | Number of females per 1000 males |
| literacy_rate | Literacy rate (%) |

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — web app framework
- [Plotly Express](https://plotly.com/python/plotly-express/) — interactive map
- [Pandas](https://pandas.pydata.org/) — data handling
- [NumPy](https://numpy.org/) — numerical operations

---

## 🚀 Run Locally

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py               # Main Streamlit app
├── india.csv            # Census dataset
├── requirements.txt     # Dependencies
└── README.md
```

---

## 💡 How to Use

1. Open the app
2. Select a **state** from the sidebar (or keep "Overall India")
3. Choose a **primary parameter** — controls bubble size
4. Choose a **secondary parameter** — controls bubble color
5. Click **Plot Graph**
