import tkinter as tk
from dashboard import DashboardFrame
from forms import FormulierenFrame
from login import LoginFrame

class MainApplication(tk.Tk):
    def __init__(self):

        # Run super for tkInter
        super().__init__()

        self.title("Belastingdienst Dashboard")
        self.geometry("670x500")

        # Container frame to hold all screens
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Configure grid weights for the container
        container.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
        container.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand

        # Dictionary to store frames
        self.frames = {}

        # Add each screen frame to the dictionary
        for F in (LoginFrame, DashboardFrame, FormulierenFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start with the login screen after frames are fully initialized
        self.switch_frame(LoginFrame)

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class] 
        frame.tkraise()  # This will bring the specified frame to the front
    
    def navigate_to(self, tab):
        # Map tabs to frame classes
        frame_mapping = {
            "Dashboard": DashboardFrame,
            "Login": LoginFrame,
            "Formulieren": FormulierenFrame
        }
        # Get the frame class for the specified tab
        frame_class = frame_mapping.get(tab)
        
        # Switch to the frame if it exists
        if frame_class:
            self.switch_frame(frame_class)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()