from flask import Flask, jsonify, render_template , request
import pandas as pd
import altair as alt

app = Flask(__name__)

df = pd.read_csv("data/lego_filtered.csv")

df['subtheme'] = df['subtheme'].where(pd.notnull(df['subtheme']), None)
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df = df[pd.to_numeric(df["year"], errors="coerce").notna()]
df['US_retailPrice'] = pd.to_numeric(df['US_retailPrice'], errors='coerce')

# Drop rows with missing or invalid values
df = df.dropna(subset=['year', 'US_retailPrice'])

#print(df['year'].dtype)
#print(df[['year']].head())
# ----------------------------
# Routes
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    records = df.to_dict(orient="records")
    return jsonify(records)

@app.route("/data_filtered")
def data_filtered():
    filtered_df = df.copy()   # ✅ FIX: use your REAL dataframe

    theme = request.args.get("theme")
    year = request.args.get("year")
    subtheme = request.args.get("subtheme")
    category = request.args.get("category")
    pieces = request.args.get("pieces")
    minifigs = request.args.get("minifigs")
    themeGroup = request.args.get("themeGroup")
    US_retailPrice = request.args.get("US_retailPrice")

    if theme:
        filtered_df = filtered_df[filtered_df["theme"] == theme]
    if year:
        filtered_df = filtered_df[filtered_df["year"] == int(year)]
    if subtheme:
        filtered_df = filtered_df[filtered_df["subtheme"] == subtheme]
    if category:
        filtered_df = filtered_df[filtered_df["category"] == category]
    if pieces:
        filtered_df = filtered_df[filtered_df["pieces"] == int(pieces)]
    if minifigs:
        filtered_df = filtered_df[filtered_df["minifigs"] == int(minifigs)]
    if themeGroup:
        filtered_df = filtered_df[filtered_df["themeGroup"] == themeGroup]
    if US_retailPrice:
        filtered_df = filtered_df[filtered_df["US_retailPrice"] == float(US_retailPrice)]

    records = filtered_df.to_dict(orient="records")
    return jsonify(records)

# ----------------------------
# Run app
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
