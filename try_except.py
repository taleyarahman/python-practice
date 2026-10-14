try:
    with open("data.txt", "r") as f:
        text = f.read()
except FileNotFoundError:
    print("File not found, starting fresh")
    text = ""