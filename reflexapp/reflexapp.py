"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

class User(rx.Base):
    name: str
    email: str
    gender: str

class State(rx.State):
    """The app state."""
    user: list[User] = [
        User(
            name="Ricardo",
            email="ricardp@test.com",
            gender="male"
        ),
        User(
            name="Laura",
            email="laura@test.com",
            gender="female"
        ),
    ]

def showUser(user: User):
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Genero"),
            ),
        ),
        rx.table.body(
            rx.foreach(State.user, showUser),
        ),
        variant = "surface",
        size = "3",
    )

app = rx.App()
app.add_page(index)
