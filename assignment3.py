from tkinter import *
from random import randint, shuffle

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
    def __init__(self, root, msInvisible, msBetween, sequenceHiding):
        self.root = root
        self.fontSize = 20
        self.fontFamily = "Helvetica"
        self.fontWeight = "bold"
        self.screenWidth = 1700
        self.defaultPadding = 20
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
        self.blocks = [self.block1, self.block2, self.block3, self.block4]
        self.blockContainer = None
        self.blockWidth = 300
        self.blockHeight = 300
        self.blockPadding = 20
        self.msInvisible = msInvisible
        self.msBetween = msBetween
        self.sequenceHiding = sequenceHiding
        self.blockColors = ["blue", "red", "green", "yellow"]
    

    def initializeScreen(self):
        self.frame = Frame(self.root, width=self.screenWidth, height=800, bg="white")
        self.frame.pack_propagate(False)  
        self.frame.pack(padx=self.defaultPadding, pady=self.defaultPadding)

        self.container1 = Frame(self.frame, width=self.screenWidth, height=30, bg="red")
        self.container1.pack_propagate(False)  
        self.container1.pack()

        self.container2 = Frame(self.frame, width=self.screenWidth, height=600, bg="gray")
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

        input1 = StringVar()
        input2 = StringVar()
        input3 = StringVar()
        input1.set(self.msInvisible) 
        input2.set(self.msBetween) 
        input3.set(self.sequenceHiding) 

        self.container3Input1 = Entry(self.container3, textvariable=input1, font=(self.fontFamily, self.fontSize, self.fontWeight))  # First input field
        self.container3Input1.grid(row=0, column=2, padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Input2 = Entry(self.container3, textvariable=input2, font=(self.fontFamily, self.fontSize, self.fontWeight))  # Second input field
        self.container3Input2.grid(row=0, column=4, padx=self.defaultPadding, pady=self.defaultPadding)
        self.container3Input3 = Entry(self.container3, textvariable=input3, font=(self.fontFamily, self.fontSize, self.fontWeight))  # Third input field
        self.container3Input3.grid(row=0, column=6, padx=self.defaultPadding, pady=self.defaultPadding)
    
    def countDown(self):
        for second in range(1):
        # for second in range(self.count):
            self.root.after(second*1000, self.countToBeginObservationalPhase)

    def startCounting(self):
        self.topMessageBox.config(text="Counting down...")
        self.startBtn.config(state="disabled")
        self.countDown()

    def convertToDot(self):
        dots = ""
        for i in range(self.count-1):
            dots += '.'
        return dots

    def beginObservationalPhase(self):
        # notes
        # first, observational phase. you click on number of squares that you have to recall later.
        # the number of squares to be clicked is specified as sequence length.
        # after hiding the correct amount of squares, you go to the recall phase.
        # in recall phase, it's the same. you click on squares. but those squares should match
        # as the squares that you hid.
        # then it's done.

        self.blockContainer = Frame(self.container2, width=800, height=700, bg="gray")
        self.blockContainer.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame in the window
        self.blockContainer.grid_rowconfigure(0, minsize=300)  # Set min height for row 0
        self.blockContainer.grid_rowconfigure(1, minsize=300)  # Set min height for row 1
        self.blockContainer.grid_columnconfigure(0, minsize=300)  # Set min width for column 0
        self.blockContainer.grid_columnconfigure(1, minsize=300)  # Set min width for column 1

        self.block1 = Frame(self.blockContainer, bg="blue")  
        self.block1.grid(row=0, column=0, sticky="nsew", padx=self.defaultPadding, pady=self.defaultPadding)  

        self.block2 = Frame(self.blockContainer, bg="red")   
        self.block2.grid(row=0, column=1, sticky="nsew", padx=self.defaultPadding, pady=self.defaultPadding) 

        self.block3 = Frame(self.blockContainer, bg="green")   
        self.block3.grid(row=1, column=0, sticky="nsew", padx=self.defaultPadding, pady=self.defaultPadding) 

        self.block4 = Frame(self.blockContainer, bg="yellow")   
        self.block4.grid(row=1, column=1, sticky="nsew", padx=self.defaultPadding, pady=self.defaultPadding) 

        self.block1.grid_propagate(False)
        self.block2.grid_propagate(False)
        self.block3.grid_propagate(False)
        self.block4.grid_propagate(False)

        self.blocks = [self.block1, self.block2, self.block3, self.block4]

        self.topMessageBox.config(text="Watch the sequence...")        
        self.bindBlocks()
        # self.randomizeSequence()

    def randomizeSequence(self):
        shuffle(self.blockColors)
        for block in range(len(self.blocks)):
            self.blocks[block].config(bg=self.blockColors[block])

    def hideBlock(self, event):
        # Access the widget that triggered the event
        self.unbindBlocks()
        blockToBeHidden = event.widget
        blockToBeHidden.grid_remove()
        blockToBeHidden.after(self.msInvisible, lambda: self.showBlock(blockToBeHidden))

        # for block in range(len(self.blocks)):
        #     if (blockToBeHidden != self.blocks[block]):
        #         self.blocks[block].grid()

    def bindBlocks(self):
        for block in range(len(self.blocks)):
            self.blocks[block].bind("<Button-1>", self.hideBlock)

    def unbindBlocks(self):
        for block in range(len(self.blocks)):
            self.blocks[block].unbind("<Button-1>")

    def showBlock(self, block):
        # Show the frame again using grid()
        block.grid()
        self.root.after(self.msBetween, self.bindBlocks)
        # there must be a delay between when blocks are all visible and a block is clicable again.


    def countToBeginObservationalPhase(self):
        if (self.count == 5):
            print ("triggered?")
            self.countingMessage.destroy()
            self.beginObservationalPhase()
            return
        
        self.countingMessage.config(text=f"{self.convertToDot()}")
        self.count = self.count - 1

def main():
    msInvisible = 1000
    msBetween = 1000
    sequenceHiding = 3

    show_duo_names()
    root = Tk()  
    window = MemoryTestWindow(root, msInvisible, msBetween, sequenceHiding)
    root.title("Memory Test")
    window.initializeScreen()
    window.initializeWidgets()
    root.mainloop()

main()