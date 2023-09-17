import pandas as pd
from millify import millify

def clean_stats(x):
    if isinstance(x, str):
        if "," in x:
            x = float(x.replace(",", "."))
        else:
            x = float(x.replace(".", ""))
    return x


def clean_honor(x):
    try:
        return int(float(x) * 1000)
    except:
        return x


def try_millify(x, precision=0):
    try:
        return millify(x, precision=precision)
    except:
        return x


def clean_data(df):
    df = df[
        [
            "name",
            "rank",
            "power_matchmaking",
            "power_before_z5",
            "power_final",
            "power_loss",
            "total_kill_points",
            "total_dead_points",
            "honor",
            "performance_index",
        ]
    ].set_index("name")
    df = df.applymap(clean_stats)
    df["honor"] = df["honor"].apply(clean_honor)
    df["total_score"] = df.total_kill_points + df.total_dead_points + 2*df.honor
    return df

def millify_stats(df):
    for col in [
        "power_matchmaking",
        "power_before_z5",
        "power_final",
        "power_loss",
        "total_kill_points",
        "honor",
    ]:
        df[col] = df[col].apply(try_millify)
    df["performance_index"] = df["performance_index"].round(1)
    for col in ["total_dead_points", "total_score"]:
        df[col] = df[col].apply(
        lambda x: try_millify(x, 0) if x < 1e9 else try_millify(x, 2)
    )
    return df

def load_and_clean_stats():
    df = pd.read_csv("assets/stats.csv")
    return clean_data(df)