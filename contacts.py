contacts = {
    "number":4,
    "students":
    [
        {"name":"Sarah Holderness", "email":"sarah@example.com"},
        {"name":"Harry Potter", "email":"harry@example.com"},
        {"name":"hermione Granger", "email":"hermione@example.com"},
        {"name":"Ron Weasley", "email":"ron@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])