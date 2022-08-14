DEBUG", "messages": structure["message"]},
                         ignore_index=True)
    if structure["type"] == "WARNING":
        df3 = df3.append({"date": structure["date"], "type": "WARNING", "messages": structure["message"]},
                         ignore_index=True)
    if structure["type"] == "