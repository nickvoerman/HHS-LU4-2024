import tkinter as tk
from dashboard import DashboardFrame
from forms import FormulierenFrame
from login import LoginFrame
from reports import ReportFrame
from changelog import ChangelogFrame
from form_detail import FormDetailFrame

class MainApplication(tk.Tk):
    def __init__(self):

        # Run super for tkInter
        super().__init__()

        self.title("Belastingdienst Dashboard")
        self.geometry("750x500")

        # Container frame to hold all screens
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Configure grid weights for the container
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to store frames
        self.frames = {}

        # Add each screen frame to the dictionary
        for F in (LoginFrame, DashboardFrame, FormulierenFrame, ReportFrame, ChangelogFrame, FormDetailFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start with the login screen after frames are fully initialized
        self.switch_frame(LoginFrame)
        
        
    def update_frame(self, old_frame_class_name, new_frame_instance):
        #remove old frame class from frames
        del self.frames[old_frame_class_name]
        
        new_frame_instance.grid(row=0, column=0, sticky="nsew")
        
        #add new frame class to frames
        self.frames[new_frame_instance.__class__] = new_frame_instance
        
    def switch_frame(self, frame_class):
        frame = self.frames[frame_class] 
        
        # This will bring the specified frame to the front
        frame.tkraise()
    
    def navigate_to(self, tab):
        # Map tabs to frame classes
        frame_mapping = {
            "Dashboard": DashboardFrame,
            "Login": LoginFrame,
            "Formulieren": FormulierenFrame,
            "Rapportages": ReportFrame
        }
        # Get the frame class for the specified tab
        frame_class = frame_mapping.get(tab)
        
        # Switch to the frame if it exists
        if frame_class:
            self.switch_frame(frame_class)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()