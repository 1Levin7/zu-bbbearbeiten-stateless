import datetime
import pytest
import helper

def test_sort():
    todos = [("Universum debuggen", "2023-09-06"),
             ("Sinn des Lebens entdecken", "2023-09-01"),
             ("Superheld werden", "2023-10-25"),
             ("Netto null", "2050-01-01")]
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    for todo in todos:
        helper.add(todo[0], todo[1])

    for i in range(len(helper.items) - 1):
        assert helper.items[i].date < helper.items[i+1].date
        assert helper.items[i].date < helper.items[i + 1].date

def test_add():
    text = "Lorem ipsum"
    date = "2023-09-02"

    helper.add(text, date)

    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)

def test_get_csv():
    helper.items.clear()
    helper.add("Essen einkaufen", "2023-09-01")
    helper.add("Lernen, Lernen, Lernen", "2023-09-02")

    csv = helper.get_csv()

    assert csv.startswith("text,date,isCompleted")
    assert "Essen einkaufen" in csv
    assert "2023-09-01" in csv
