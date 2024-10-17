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
    def __init__(self, root):
        self.root = root
        self.fontSize = 20
        self.fontFamily = "Helvetica"
        self.fontWeight = "bold"
        self.screenWidth = 1200
        self.defaultPadding = 10
        self.count = 5
        self.frame = None
        self.container1 = None
        self.container2 = None
        self.container3 = None
        self.container3Label1 = None
        self.container3Label2 = None
        self.container3Label3 = None
        self.container3Input1 = None
        self.container3Input2 = None
        self.container3Input3 = None
        self.topMessageBox = None
        self.countingMessage = None
        self.startBtn = None
        self.block1 = None
        self.block2 = None
        self.block3 = None
        self.block4 = None
        self.blockContainer = None
        self.blockWidth = 20
        self.blockHeight = 2

    def initializeScreen(self):
        self.frame = Frame(self.root, width=self.screenWidth, height=500, bg="white")
        self.frame.pack_propagate(False)  
        self.frame.pack(padx=self.defaultPadding, pady=self.defaultPadding)

        self.container1 = Frame(self.frame, width=self.screenWidth, height=30, bg="red")
        self.container1.pack_propagate(False)  
        self.container1.pack()

        self.container2 = Frame(self.frame, width=self.screenWidth, height=200, bg="gray")
        self.container2.pack_propagate(False)
        self.container2.pack(fill="both", expand=True)

        self.container3 = Frame(self.frame, width=self.screenWidth, height=200, bg="green")
        self.container3.pack_propagate(False)
        self.container3.pack()

        return

    def initializeWidgets(self):
        
        self.countingMessage = Label(self.container2, text="counting", font=(self.fontFamily, self.fontSize, self.fontWeight))
        self.countingMessage.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame in the window

        self.topMessageBox = Label(self.container1, text="Click 'start' to begin the memory test.", font=(self.fontFamily, self.fontSize, self.fontWeight))
        self.topMessageBox.pack(side="top")  # Place the label at the top of the frame

        self.startBtn = Button(self.container3, text="Start", bg="lightgreen", font=(self.fontFamily, self.fontSize, self.fontWeight), command=self.startCounting)  # startBtn
        self.startBtn.grid(row=0, column=0)

        self.container3Label1 = Label(self.container3, text="ms invisible: ", font=(self.fontFamily, self.fontSize, self.fontWeight))  # First label
        self.container3Label1.grid(row=0, column=1, padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Label2 = Label(self.container3, text="ms between: ", font=(self.fontFamily, self.fontSize, self.fontWeight))  # Second label
        self.container3Label2.grid(row=0, column=3, padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Label3 = Label(self.container3, text="sequence length", font=(self.fontFamily, self.fontSize, self.fontWeight))  # Third label
        self.container3Label3.grid(row=0, column=5, padx=self.defaultPadding, pady=self.defaultPadding)

        self.container3Input1 = Entry(self.container3)  # First input field
        self.container3Input1.grid(row=0, column=2, padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Input2 = Entry(self.container3)  # Second input field
        self.container3Input2.grid(row=0, column=4, padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Input3 = Entry(self.container3)  # Third input field
        self.container3Input3.grid(row=0, column=6, padx=self.defaultPadding, pady=self.defaultPadding)
    
    def startCounting(self):
        self.topMessageBox.config(text="Counting down...")
        self.startBtn.config(state="disabled")
        self.countToBeginObservationalPhase()
        self.root.after(1000, self.countToBeginObservationalPhase)
        self.root.after(2000, self.countToBeginObservationalPhase)
        self.root.after(3000, self.countToBeginObservationalPhase)
        self.root.after(4000, self.countToBeginObservationalPhase)

    def convertToDot(self):
        dots = ""
        for i in range(self.count):
            dots += '.'
        return dots

    def beginObservationalPhase(self):
        self.blockContainer = Frame(self.container2, width=800, height=400, bg="gray")
        self.blockContainer.pack_propagate(False)  # Prevent container2 from resizing to fit its contents
        self.blockContainer.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame in the window

        self.block1 = Label(self.blockContainer, font=(self.fontFamily, self.fontSize, self.fontWeight), bg="red", width=self.blockWidth, height=self.blockHeight)  
        self.block1.grid(row=0, column=0, padx=self.defaultPadding, pady=self.defaultPadding)  

        self.block2 = Label(self.blockContainer, font=(self.fontFamily, self.fontSize, self.fontWeight), bg="blue", width=self.blockWidth, height=self.blockHeight) 
        self.block2.grid(row=0, column=1, padx=self.defaultPadding, pady=self.defaultPadding) 

        self.block3 = Label(self.blockContainer, font=(self.fontFamily, self.fontSize, self.fontWeight), bg="black", width=self.blockWidth, height=self.blockHeight)  
        self.block3.grid(row=1, column=0, padx=self.defaultPadding, pady=self.defaultPadding)  

        self.block4 = Label(self.blockContainer, font=(self.fontFamily, self.fontSize, self.fontWeight), bg="white", width=self.blockWidth, height=self.blockHeight) 
        self.block4.grid(row=1, column=1, padx=self.defaultPadding, pady=self.defaultPadding) 

    def countToBeginObservationalPhase(self):
        if (self.count == 1):
            self.countingMessage.destroy()
            self.beginObservationalPhase()
            return

        self.countingMessage.config(text=f"{self.convertToDot()}")
        self.count = self.count - 1

def main():
    show_duo_names()

    root = Tk()  
    window = MemoryTestWindow(root)
    root.title("Memory Test")
    window.initializeScreen()
    window.initializeWidgets()
    root.mainloop()

main()