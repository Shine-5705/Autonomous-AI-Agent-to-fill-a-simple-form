# Autonomous-AI-Agent-to-fill-a-simple-form

This Python script automates the filling of a web form using Selenium and generates text using the OpenAI GPT-3.5-turbo model for specific fields.

## Prerequisites

- Python 3.x installed on your system
- Pip package manager
- Chrome browser installed (for Selenium web automation)
- Chromedriver installed (for Selenium web automation)

## Installation

1. Clone this repository to your local machine:

    ```
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```
    cd Autonomous-AI-Agent-to-fill-a-simple-form

    ```

3. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Set up a `.env` file with your OpenAI API key:

    ```
    OPENAI_API_KEY=your-api-key
    ```

2. Run the Python script:

    ```
    python main.py
    ```

3. The script will open a Chrome browser, fill out the specified web form, and submit it. Make sure to adjust the XPath selectors and input data according to your specific form.

## Configuration

- Modify the XPath selectors and input data in the `main.py` script to match your web form.
- Adjust wait times (`time.sleep()`) as needed to ensure proper loading of elements.

