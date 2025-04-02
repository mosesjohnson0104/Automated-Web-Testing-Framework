🚀 Automated Web Testing Framework



📌 Project Overview
This Automated Web Testing Framework is built using Python, Selenium WebDriver, and PyTest to streamline web application testing. The framework enhances efficiency by automating test execution, reducing manual effort, and integrating with CI/CD pipelines.

⚙️ Tech Stack
✅ Programming Language: Python 🐍
✅ Testing Framework: PyTest 🧪
✅ Automation Tool: Selenium WebDriver 🌐
✅ CI/CD Integration: Jenkins 🚀

📂 Project Structure
Automated-Web-Testing-Framework/
│── tests/                  # Contains all test cases
│   ├── test_login.py        # Example: Login functionality test
│   ├── test_search.py       # Example: Search functionality test
│
│── pages/                   # Implements Page Object Model (POM)
│   ├── login_page.py        # Login Page elements & methods
│   ├── search_page.py       # Search Page elements & methods
│
│── config/                  # Configuration files
│   ├── config.yaml          # Stores environment settings
│
│── utils/                   # Utility scripts
│   ├── driver_setup.py      # Manages WebDriver setup
│
│── requirements.txt         # Dependencies for the project
│── README.md                # Documentation
│── .gitignore               # Excluded files

🛠 Setup & Installation
Prerequisites
Before running the project, ensure you have:

✅ Python 3.x → Download Here
✅ Google Chrome → Download Here
✅ ChromeDriver (matching your Chrome version) → Download Here
✅ Git (optional for cloning) → Download Here

Installation Steps
1️⃣ Clone the repository
git clone https://github.com/mosesjohnson0104/Automated-Web-Testing-Framework.git
2️⃣ Navigate to the project directory
cd Automated-Web-Testing-Framework
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Set up WebDriver path
Open utils/driver_setup.py and update the ChromeDriver path.

🚀 Running Tests
Run all test cases
pytest tests/
Run a specific test file
pytest tests/test_login.py
Run tests and generate an HTML report
pytest --html=report.html --self-contained-html

🌟 Features
✔️ Page Object Model (POM) for maintainability
✔️ Data-Driven Testing with PyTest
✔️ Cross-Browser Support (Chrome, Firefox, Edge)
✔️ Jenkins CI/CD Integration for automated testing

🏗 Contributing
👨‍💻 Contributions are welcome! Follow these steps:

Fork the repository

Create a new branch (git checkout -b feature-branch)

Commit your changes (git commit -m "Added new feature")

Push to the branch (git push origin feature-branch)

Open a Pull Request 🚀

📞 Contact
📧 Email: mosesjohnson.nixon@gmail.com
🔗 LinkedIn: Moses Johnson
👨‍💻 GitHub: MosesJohnson0104

