# Netflix Data Visualization — README

**Author:** Adebowale Saheed Badru
**Institution/Program:** Nexford University / Master of Science, Data Analytics
**Course:** BAN 6420 — Programming in R & Python (Module 4)
**Date:** November 2025

---

## 🎯 Project Overview

This project explores the **Netflix Titles Dataset** to uncover insights about content distribution by **genre** and **rating**. It fulfills the Module 4 requirement for visual analytics using both **Python** and **R**, focusing on clean, readable code and clear visualization.

**Key Objectives:**

* Prepare and clean the dataset for analysis.
* Perform exploratory data analysis (EDA).
* Visualize top genres and ratings distribution using Python (Seaborn/Matplotlib).
* Reproduce one visualization (ratings distribution) in R using ggplot2.

---

## 🧰 Environment Setup

### 1. Create Virtual Environment

```bash
python -m venv .venv
& .\.venv\Scripts\Activate.ps1  # PowerShell (Windows)
# or for macOS/Linux
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
pandas
numpy
matplotlib
seaborn
jupyter
```

### 3. R Libraries

```r
install.packages(c("readr", "dplyr", "ggplot2"))
```

---

## 📦 Project Structure

```
netflix-visuals/
├─ data/
│  └─ netflix_data.csv
├─ src/
│  ├─ prep.py
│  ├─ clean.py
│  ├─ explore.py
│  └─ visualize.py
├─ r/
│  └─ visualize_genres.R
├─ outputs/
├─ README.md
└─ requirements.txt
```

---

## 🧹 Data Preparation & Cleaning

### Step 1: Prepare the Dataset

Rename or unzip the dataset to maintain a consistent naming convention.

```bash
python -m src.prep --in data/netflix_data.csv --out data/Netflix_shows_movies.csv
```

### Step 2: Clean the Dataset

```bash
python -m src.clean --in data/Netflix_shows_movies.csv --out data/Netflix_clean.csv
```

**Cleaning Operations:**

* Removed extra spaces in text fields.
* Converted `rating` to uppercase for consistency.
* Transformed `date_added` to datetime.
* Replaced missing `country` values with **Unknown**.
* Replaced missing `rating` values with **UNRATED**.
* Dropped rows missing essential fields (`title`, `type`).

**Reflection:**

> I chose `title` and `type` as essential columns because missing them made analysis unreliable. Dropping these rows ensured better grouping accuracy later.

---

## 🔍 Exploratory Data Analysis (EDA)

Explore the cleaned dataset to understand its structure and identify key trends.

```bash
python -m src.explore --in data/Netflix_clean.csv
```

**What I Explored:**

* Dataset shape and column types.
* Count of missing values per column.
* Movie vs TV Show distribution.
* Most common genres.

**Reflection:**

> The dataset contained more movies than TV shows, with genres like *Dramas*, *Comedies*, and *International Movies* dominating. Most content was rated *TV-MA* or *TV-14*.

---

## 📊 Data Visualization (Python)

Create visuals using Seaborn and Matplotlib.

```bash
python -m src.visualize --in data/Netflix_clean.csv --outfig outputs/ --topn 12
```

**Visuals Produced:**

1. `top_genres.png` — Top 10 most common genres.
2. `rating_distribution.png` — Ratings distribution.

**Reflection:**

> I used horizontal bars for genres to make long names easier to read and rotated x-labels for ratings to prevent overlap. Keeping colors simple made the visuals more professional and accessible.

---

## 📈 Visualization in R (Integration)

Replicate the Ratings Distribution chart in R.

```bash
Rscript r/visualize_genres.R data/Netflix_clean.csv outputs/
```

**Output:** `rating_distribution_R.png`

**Reflection:**

> The R plot matched the Python output closely, though ggplot2 applied a cleaner minimalist theme by default. This exercise helped me compare syntax and defaults across both languages.

---

## 💾 GitHub & Submission

### Upload to GitHub

```bash
git init
git add .
git commit -m "Initial commit - Netflix Data Visualization"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Netflix-Visuals.git
git push -u origin main
```

### Zip for Canvas Submission

```bash
cd netflix-visuals
zip -r Netflix_DataViz_SaheedBadru.zip .
```

**Final Deliverables:**

* `src/` — Python scripts
* `r/` — R script
* `outputs/` — Visuals
* `README.md` — Documentation
* `requirements.txt` — Dependencies

---

## 🧠 Key Learnings

* Cleaning and organizing data early made visualizations smoother.
* Converting strings and dates correctly reduced type errors.
* Working across Python and R built my confidence in data interoperability.
* Visual storytelling reinforced my understanding of descriptive analytics.

**License:** Educational use for coursework at Nexford University.
