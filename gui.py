import tkinter as tk
import draft
import player

def main():
    root = tk.Tk()

    root.title("Fantasy Football App")
    #root.configure(background="navy")
    root.geometry('350x200')

    def button_clicked():
        print("Button clicked!")


    draftButton = tk.Button(root, 
                    text="Draft Script", 
                    command=draft.draftGui,
                    activebackground="blue", 
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

    draftButton.pack(padx=20, pady=20)

    playerButton = tk.Button(root, 
                    text="Player Analysis", 
                    command=player.playerGui,
                    activebackground="blue", 
                    activeforeground="white",
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

    playerButton.pack(padx=10, pady=10)


    root.mainloop()

if __name__ == "__main__":
    main()