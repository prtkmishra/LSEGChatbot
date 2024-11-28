# **LSEG Stock Chatbot**

A conversational chatbot built with Streamlit to provide stock information from various stock exchanges (LSEG, NASDAQ, NYSE). 
The app allows users to select stock exchanges, view stock data, and get stock values interactively.

---

## **Features**
- Conversational chatbot interface.
- Navigate between Home Menu and Stock Menu.
- View stock data dynamically based on user queries.
- Robust error handling for invalid inputs.
- Lightweight and modular design for maintainability.

---

## **Technologies Used**
- **Python**: Core programming language.
- **Streamlit**: For building the interactive web app.
- **Pandas**: For data processing.
- **JSON**: For storing and loading stock data.
- **Logging**: For tracking application activity.

---

## **Approach**
- Convert the json to a dataframe
- Pandas data frame provide a optimized way to access data
- Dataframe provide scope for scalability in the data
- To access interim data, temp folder is created for storing temp information (such as to enable home and  go back options)
- temp data was used because streamlit could not access cache memory as of now. 

## **Getting Started**

### **Prerequisites**
Ensure the following are installed on your system:
- Python 3.11+
- pip (Python package manager)
- Git (for cloning the repository)

### **Installation Steps**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/prtkmishra/LSEGChatbot.git
   cd lseg-stock-chatbot
   ```
   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   streamlit run lsegchatbot.py
   ```
2. **Access the App: Open your browser and navigate to http://localhost:8501**
3. **File Structure**
```plaintext
LSEGChatbot/
            │
            ├── lsegchatbot.py                         # Main Streamlit application
            ├── process_data.py                        # Data processing module
            ├── requirements.txt                       # Python dependencies
            ├── ./log/lsegchatbot.log                  # (Generated) Log file for debugging
            ├── ./data/(TC3)Chatbot - stock data.json  # JSON file containing stock data
            ├── ./temp/                                # Store temp data
            ├── Dockerfile                             # Docker configuration file
            ├── README.md                              # Project documentation
            └── .dockerignore                          # Files to exclude from Docker builds
```
 5. **Key Functionalities**:
### **a. Home Menu**
    - Displays a list of stock exchanges (LSEG, NASDAQ, NYSE).
    - Users can select a stock exchange to view available stocks.
    - Select and copy the text

### **b. Stock Menu**
    - Provides a list of five stocks for the selected exchange.
    - Displays the current value of the selected stock.
    - Select and copy the text
    
### **c. Error Handling**
    - Handles invalid inputs gracefully.
    - Provides feedback for unsupported queries.

### **d. Navigation**
    - Users can return to the Home Menu or go back to the Stock Menu at any time.

### **e. Logging**
    - All user interactions and errors are logged to the ./data/lsegchatbot.log file for monitoring and debugging purposes.
---

5. **Further Enhancements**
   - Using cache memory to remove the temp data folder usage
   - Taking user inputs using intellisense
      
6. **Known Issues**
   - Chat history is not maintained because streamlit has an issue with rendering pandas dataframe in the chat history.
   - The issue exists even with using 'type' : 'table'
