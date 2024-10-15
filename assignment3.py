from tkinter import *
from random import randint

# solution version 1: without extensions

def show_duo_names():
    print()
    print('┌─────────────────────┬───────────────────────┐')
    print('│ 0HV120 assignment 3 │ Memory Test           │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 1       │ name 1                │')
    print('├─────────────────────┼───────────────────────┤')
    print('│ duo partner 2       │ name 2                │')
    print('└─────────────────────┴───────────────────────┘')


class MemoryTestWindow:
    def __init__(self):
        return  # replace with you code

def createRow(root, rows):
    for row in range(rows):
        root.rowconfigure(row, weight=row+1)

def createColumn(root, columns):
    for column in range(columns):
        root.rowconfigure(column, weight=column+1)

def main():
    show_duo_names()

    root = Tk()  # Create the main window
    root.title("Memory Test")

    # Configure row weights for varying row sizes
    createRow(root, 3)
    # Configure the column size
    # root.columnconfigure(0, weight=1)

    # Create labels for each row with different background colors
    rowWidth = 1000
    rowHeight = 20
    midRowHeight = 300
    defaultPadding = 5

    # Create the first label with a frame for the inner label
    row1 = Label(root)
    row1.grid(row=0, column=0)

    # Create the second label
    row2 = Label(root, bg="lightgreen")
    row2.grid(row=1, column=0, sticky="nsew")

    # Create the third label
    row3 = Label(root)
    row3.grid(row=2, column=0)

    # Create a frame inside the first label with specified width and height
    frame1 = Frame(row1, width=rowWidth, height=rowHeight)
    frame1.pack(padx=defaultPadding, pady=defaultPadding)  # Fill the frame and expand

    # Create a frame inside the second label with specified width and height
    frame2 = Frame(row2, width=rowWidth, height=midRowHeight, bg="lightgreen")
    frame2.pack(padx=defaultPadding, pady=defaultPadding)  # Fill the frame and expand

    # Create an inner label to add text inside the frame
    frame1Container = Label(frame1)
    frame1Container.pack(pady=defaultPadding)  # Padding around the inner label

    frame1ContainerMessage = Label(frame1Container, text="Click 'start' to begin the memory test.", font=("Helvetica", 20, "bold"))
    frame1ContainerMessage.pack(side="top")  # Place the label at the top of the frame

    # Create a frame inside the third label with specified width and height
    frame3 = Frame(row3, width=rowWidth, height=rowHeight)
    frame3.pack(padx=defaultPadding, pady=defaultPadding)  # Fill the frame and expand

    frame3Container = Label(frame3)
    frame3Container.pack(side="bottom", pady=defaultPadding, expand=True)  # Padding around the inner label

    # Create the new widgets in the specified order
    frame3StartBtn = Button(frame3Container, text="Start", bg="lightgreen", font=("Helvetica", 20, "bold"))  # frame3StartBtn
    frame3StartBtn.grid(row=0, column=0, padx=defaultPadding, pady=defaultPadding, sticky="ew")

    frame3Label1 = Label(frame3Container, text="ms invisible: ", font=("Helvetica", 20, "bold"))  # First label
    frame3Label1.grid(row=0, column=1, padx=defaultPadding, pady=defaultPadding)
    frame3Label2 = Label(frame3Container, text="ms between: ", font=("Helvetica", 20, "bold"))  # Second label
    frame3Label2.grid(row=0, column=3, padx=defaultPadding, pady=defaultPadding)
    frame3Label3 = Label(frame3Container, text="sequence length", font=("Helvetica", 20, "bold"))  # Third label
    frame3Label3.grid(row=0, column=5, padx=defaultPadding, pady=defaultPadding)

    frame3Input1 = Entry(frame3Container)  # First input field
    frame3Input1.grid(row=0, column=2, padx=defaultPadding, pady=defaultPadding)
    frame3Input2 = Entry(frame3Container)  # Second input field
    frame3Input2.grid(row=0, column=4, padx=defaultPadding, pady=defaultPadding)
    frame3Input3 = Entry(frame3Container)  # Third input field
    frame3Input3.grid(row=0, column=6, padx=defaultPadding, pady=defaultPadding)

    root.mainloop()

main()