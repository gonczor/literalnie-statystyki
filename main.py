from collections import Counter
import locale

import matplotlib.pyplot as plt


locale.setlocale(locale.LC_ALL, "pl_PL.UTF-8")


def get_count() -> tuple[dict, int, int]:
    words = ""
    ends_with_a = 0
    double_letters = 0

    with open("słowa.txt") as f:
        for line in f.readlines():
            word = line.rstrip()
            words += word
            if word.endswith("a"):
                ends_with_a += 1
            if len(set(word)) < len(word):
                double_letters += 1

    histogram = Counter(words)
    sorted_histogram = {
        key: round(histogram[key]/len(histogram)*100)
        for key in sorted(histogram)
    }
    return sorted_histogram, ends_with_a, double_letters


def ascii_histogram(count: dict):
    for k in count.keys():
        print('{0} {1}'.format(k, '+' * count[k]))


def graphic_histogram(count: dict):
    plt.bar(range(len(count)), list(count.values()), tick_label=list(count.keys()))
    plt.title("Częstotliwość występowania liter")
    plt.xlabel("Litera")
    plt.ylabel("% wystąpień")
    for i, v in enumerate(count.values()):
        plt.text(i, v, f"{v}%", ha="center")
    plt.show()


count, ends_with_a, double_letters = get_count()
print(f"Ends with a in {round(ends_with_a/len(count)*100)}% of all words")
print(f"Words with double letters are in {round(double_letters/len(count)*100)}% of all words")
graphic_histogram(count)
