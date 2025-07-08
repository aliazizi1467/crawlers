import json, os, time
from datetime import datetime, timedelta
from pathlib import Path

# شناسه اختصاصی خزنده ۳
CRAWLER_ID = "crawler_03"

# زمان‌بندی وظایف مختلف خزنده
TASK_TIMES = {
    "task_1": timedelta(days=2),      # 2 روز قبل بازی
    "task_2": timedelta(hours=13),    # 13 ساعت قبل بازی
    "task_3": timedelta(minutes=13),  # 13 دقیقه قبل بازی
    "task_4": timedelta(minutes=0)    # در پایان بازی (FT)
}

def log(msg):
    print(f"[{CRAWLER_ID}] {msg}")

def load_games():
    with open("games_master.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_file(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def assign_game(game):
    return game.get("assigned_to") in [None, CRAWLER_ID]

def should_do_task(game, task, now_utc):
    start = datetime.fromisoformat(game["start_time_utc"].replace("Z", "+00:00"))
    deadline = start - TASK_TIMES[task]
    return (
        now_utc >= deadline and 
        game["status"].get(task) is None and 
        assign_game(game)
    )

def run():
    now = datetime.utcnow()
    games = load_games()
    results_model_x = []
    results_model_final = []

    for game in games:
        for task in TASK_TIMES:
            if should_do_task(game, task, now):
                log(f"✅ {task} started for game {game['game_id']}")
                game["status"][task] = str(now)
                game["assigned_to"] = CRAWLER_ID

                if task == "task_4":
                    results_model_final.append({
                        "game_id": game["game_id"],
                        "report": "✔ پایان بازی ثبت شد (FT)",
                        "utc_time": str(now)
                    })
                else:
                    results_model_x.append({
                        "game_id": game["game_id"],
                        "country": game["country"],
                        "teams": game["teams"],
                        "time_local": game.get("start_time_local", "unknown"),
                        "A_B_C": {
                            "home": game["home"],
                            "away": game["away"]
                        },
                        "task": task,
                        "utc_time": str(now)
                    })

    save_file(f"outbox/{CRAWLER_ID}_to_model_x.json", results_model_x)
    save_file(f"outbox/{CRAWLER_ID}_to_final_model_log.json", results_model_final)
    save_file("games_master.json", games)

run()
