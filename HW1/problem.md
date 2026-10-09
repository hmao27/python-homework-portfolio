# Library Study Room Reservation

Write a Python program that decides whether a student is allowed to reserve a study room in the library.

The program needs to consider:

- The number of hours they want to reserve the room.
- The number of people in the group.
- Whether the student has overdue library books.
- Whether the reservation is for after 10 p.m.

Input is only valid when the group has at least 1 and no more than 8 people. The reservation duration must be at least 1 hour and no more than 4 hours.

The program needs to follow these rules:

1. If the inputs are invalid, print `Invalid input.`
2. If the student has overdue library books, reject the reservation and print `Reservation rejected: you have overdue library books.`
3. If the reservation is after 10 p.m., reject the reservation and print `too late!`
4. If the group has more than 6 people, print a warning that a larger room may be needed.
5. Otherwise, approve the reservation.

## Purpose of the Problem

This problem is about Boolean expressions, functions, input validation, and `if`/`elif`, which is pretty similar to the exercises we have in this week's assignment. The student must combine several conditions instead of satisfying only one simple rule.

The most difficult part will be that there are so many conditions and rules to follow. Besides rejection and approval, there are also warning situations. By doing it, students may have a better understanding of the knowledge listed above.
