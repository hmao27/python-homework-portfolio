"""Library study room reservation problem (corrected from original answer key)."""


def valid_inputs(hours, people):
    return hours >= 1 and hours <= 4 and people >= 1 and people <= 8


def reservation_advice(hours, people, overdue_books, after_10pm):
    if not valid_inputs(hours, people):
        print("Invalid input.")
        return

    if overdue_books:
        print("Reservation rejected: you have overdue library books.")
    elif after_10pm:
        print("too late!")
    elif people > 6:
        print("Reservation approved, but you may need a larger room.")
    else:
        print("Reservation approved.")


if __name__ == "__main__":
    reservation_advice(2, 4, False, False)
