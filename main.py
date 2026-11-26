import os

LINE = "Incident report: the unmatched sock was a threat to household order and was neutralized. Its partner has been filed as a missing person. I regret nothing; I remember nothing."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
