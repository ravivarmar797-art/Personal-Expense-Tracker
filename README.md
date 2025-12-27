# Personal Expense Tracker

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A robust command-line expense tracking application built with Python, featuring persistent data storage and comprehensive CRUD operations for personal financial management.

## 🎯 Overview

Personal Expense Tracker is a lightweight, yet powerful CLI application designed to help users efficiently track, manage, and analyze their daily expenses. Built with simplicity and reliability in mind, it provides an intuitive interface for financial record-keeping without the overhead of complex database systems.

## ✨ Key Features

### Core Functionality
- **Expense Management**: Full CRUD operations (Create, Read, Update, Delete) for expense records
- **Persistent Storage**: JSON-based data persistence ensures data integrity across sessions
- **Category Filtering**: Filter and view expenses by custom categories
- **Financial Analytics**: Real-time total spending calculations with category-wise breakdowns
- **Data Validation**: Comprehensive input validation to maintain data quality and prevent errors

### User Experience
- **Interactive CLI**: Menu-driven interface with clear navigation
- **Formatted Output**: Tabular data presentation with aligned columns for better readability
- **Confirmation Prompts**: Safety mechanisms for destructive operations (delete)
- **Error Handling**: Graceful error management with user-friendly feedback

## 🛠️ Technical Stack

- **Language**: Python 3.7+
- **Data Format**: JSON
- **Storage**: File-based persistence
- **Architecture**: Modular functional programming

## 📋 Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses Python standard library only)

## 🚀 Installation

### Clone the Repository
```bash
git clone https://github.com/ravivarmar797-art/Personal-Expense-Tracker.git
cd Personal-Expense-Tracker
```

### Verify Python Installation
```bash
python --version
# or
python3 --version
```

### Run the Application
```bash
python expense_tracker.py
# or
python3 expense_tracker.py
```

## 📖 Usage Guide

### Main Menu Options

```
------personal expense tracker-------
1. Add expenses
2. View expenses
3. View by category
4. Show the total
5. Exit
6. Edit expense
7. Delete expense
```

### 1. Adding an Expense
- Enter amount (must be positive number)
- Provide item name (cannot be empty)
- Specify category (e.g., Food, Transport, Entertainment)
- Input date in YYYY-MM-DD format

**Example:**
```
Enter amount: 120.00
Enter item name: Chicken Rice
Enter category: Food
Enter date (YYYY-MM-DD): 2025-12-27
```

### 2. Viewing All Expenses
Displays all recorded expenses in a formatted table with columns:
- Date
- Item Name
- Category
- Amount

### 3. Filtering by Category
Search and display expenses belonging to a specific category:
```
Enter category to filter: Food
```

### 4. Viewing Total Spending
Displays:
- Overall total spending
- Category-wise breakdown with individual totals

### 5. Editing an Expense
1. View expenses with index numbers
2. Select expense by index
3. Update any field (press Enter to keep existing value)
4. Changes are saved automatically

### 6. Deleting an Expense
1. View expenses with index numbers
2. Select expense by index
3. Confirm deletion (y/n)
4. Record is permanently removed

### 7. Exit
Saves all changes and closes the application gracefully.

## 📊 Data Structure

### Expense Object Schema
```json
{
  "item": "string",
  "amount": float,
  "category": "string",
  "date": "YYYY-MM-DD"
}
```

### Storage File
All expenses are stored in `expenses.json` in the project root directory.

## 🏗️ Project Architecture

```
Personal-Expense-Tracker/
│
├── expense_tracker.py       # Main application logic
├── expenses.json            # Persistent data storage (auto-generated)
├── README.md                # Project documentation
└── .gitignore              # Git ignore rules (optional)
```

### Core Functions

| Function | Purpose |
|----------|---------|
| `save_to_file()` | Persists expense data to JSON file |
| `load_from_file()` | Loads existing expenses on startup |
| `show_expenses_with_index()` | Displays expenses with index numbers for editing/deleting |

## 🔒 Input Validation

The application implements multiple validation layers:

- **Amount Validation**: Ensures positive numeric values
- **Empty Field Prevention**: Rejects empty item names and categories
- **Date Format Validation**: Enforces YYYY-MM-DD format
- **Index Validation**: Prevents out-of-range index access
- **Type Checking**: Handles ValueError exceptions for numeric inputs

## 🎓 Learning Outcomes

This project demonstrates proficiency in:

- **File I/O Operations**: Reading from and writing to JSON files
- **Data Structures**: Working with lists and dictionaries
- **Error Handling**: Try-except blocks and user input validation
- **Modular Programming**: Function-based code organization
- **Control Flow**: While loops, conditional statements, and menu systems
- **String Formatting**: Aligned output using f-strings
- **Data Persistence**: Maintaining state across program executions

## 🐛 Known Issues & Limitations

- Date validation checks format but not actual date validity (e.g., 2025-13-45 would pass)
- No built-in backup or export functionality
- Category names are case-sensitive for filtering
- No multi-user support or authentication

## 🔮 Future Enhancements

### Planned Features
- [ ] Enhanced date validation using `datetime` module
- [ ] Monthly/yearly expense reports
- [ ] Budget setting and overspending alerts
- [ ] Data export to CSV/Excel formats
- [ ] Search functionality by item name or date range
- [ ] Graphical visualization of spending patterns
- [ ] Multi-currency support
- [ ] Recurring expense tracking
- [ ] Database integration (SQLite)
- [ ] Web-based GUI using Flask/Django

### Long-term Vision
- Cloud synchronization
- Mobile application
- Receipt scanning and OCR
- Machine learning for expense prediction

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ravi Varma**
- GitHub: [@ravivarmar797-art](https://github.com/ravivarmar797-art)
- Specialization: AI & Data Science
- Skills: Python | Machine Learning | Problem Solving

## 🙏 Acknowledgments

- Built as a milestone project for mastering Python fundamentals
- Inspired by the need for simple, effective personal finance management
- Thanks to the Python community for excellent documentation

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: ravivarmar797@gmail.com

---

<div align="center">

**If you find this project useful, please consider giving it a ⭐!**

Made with ❤️ and Python

</div>