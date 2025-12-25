sozlar = ["kitob", "dastur", "AI", "hello", "python"]
filter_sozlar = [s for s in sozlar if len(s) > 5]
print("5 dan katta uzunlikdagilar:", filter_sozlar)