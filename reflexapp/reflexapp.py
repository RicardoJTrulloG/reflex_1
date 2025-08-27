"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from collections import Counter

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
    user_for_graph: list[dict] = []

    def add_user(self, form_data: dict):
        self.user.append(User(**form_data))
        self.transform_data()

    def transform_data(self):
        gender_counts = Counter(
            user.gender for user in self.user
        )

        self.user_for_graph = [
            {"name": gender_group, "value": count}
            for gender_group, count in gender_counts.items()
        ]

def graph():
    return rx.recharts.bar_chart(
        rx.recharts.bar(
            data_key="value",
            stroke=rx.color("accent", 9),
            fill=rx.color("accent",8)
        ),
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(),
        data=State.user_for_graph,
        width="100%",
        height=250,
    )

def showUser(user: User):
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

def form():
    return rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.icon("plus", size=26),
                    rx.text("add User", size="4"),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Añadir un nuevo usuario",
            ),
            rx.dialog.description(
                "Llenar la información del usuario",
            ),
        
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="Nombre", 
                        name="name", 
                        required=True
                    ),
                    rx.input(
                        placeholder="Email", 
                        name="email",
                    ),
                    rx.select(
                        ['male','female'],
                        placeholder="gender",
                        name="gender"
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.dialog.close(
                            rx.button("Submit", type="submit"),
                        ),
                        spacing="3",
                        justify="end",
                    ),
                    direction="column",
                    spacing="4", 
                ),
                on_submit=State.add_user,
                reset_on_submit=False,       
            ),
            max_width="450px",
        ),
    )
    


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        form(),
        rx.table.root(
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
        ),
        graph(),
        justify="center",
        align="center",
    )

app = rx.App()
app.add_page(index)
