import unittest
from main import MainApplication
from login import LoginFrame
from dashboard import DashboardFrame
from forms import FormulierenFrame
from reports import ReportFrame

class TestMainApplication(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the main application
        self.app = MainApplication()
        # Create a forms frame instance
        self.formulieren_frame = FormulierenFrame(self.app, self.app)
        # Initialize the login frame
        self.app.frames[LoginFrame] = LoginFrame(self.app, self.app)

    def test_switch_frame(self):
        self.app.switch_frame(LoginFrame)
        self.assertIsInstance(self.app.frames[LoginFrame], LoginFrame)

    def test_verify_login(self):
        # Get the login frame
        login_frame = self.app.frames[LoginFrame]
        # Input correct credentials
        login_frame.entry_username.insert(0, "admin")
        login_frame.entry_password.insert(0, "password")
        # Attempt login
        login_frame.verify_login()
        # Verify that we're redirected to dashboard
        self.assertIsInstance(self.app.frames[DashboardFrame], DashboardFrame)
        
    def test_failed_login(self):
        # Get the login frame
        login_frame = self.app.frames[LoginFrame]
        # Input incorrect credentials
        login_frame.entry_username.insert(0, "wrong")
        login_frame.entry_password.insert(0, "wrong")
        # Attempt login
        login_frame.verify_login()
        # Verify error message is displayed
        self.assertEqual(login_frame.error_label.cget("text"), "Onjuiste gebruikersnaam of wachtwoord.")

    def test_navigation(self):
        # Test navigation to Dashboard
        self.app.navigate_to("Dashboard")
        self.assertIsInstance(self.app.frames[DashboardFrame], DashboardFrame)
        
        # Test navigation to Forms
        self.app.navigate_to("Formulieren")
        self.assertIsInstance(self.app.frames[FormulierenFrame], FormulierenFrame)
        
        # Test navigation to Reports
        self.app.navigate_to("Rapportages")
        self.assertIsInstance(self.app.frames[ReportFrame], ReportFrame)
        

class TestIntegrationFlow(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the main application
        self.app = MainApplication()
        # Initialize the login frame
        self.app.frames[LoginFrame] = LoginFrame(self.app, self.app)

    def test_full_application_flow(self):
        # Get the login frame
        login_frame = self.app.frames[LoginFrame]
        # Input correct credentials
        login_frame.entry_username.insert(0, "admin")
        login_frame.entry_password.insert(0, "password")
        # Attempt login
        login_frame.verify_login()
        
        # Verify that the DashboardFrame was created and exists
        self.assertIsInstance(self.app.frames[DashboardFrame], DashboardFrame)
        self.assertEqual(self.app.frames[DashboardFrame].winfo_exists(), True)

if __name__ == '__main__':
    unittest.main()