# Wanderlust-Travel-Planner-Assignment

The Wanderlust Travel Planner API is a backend application created with Flask Web Framework, that serves users to plan their trips, manage destinations, add or delete itineraries, track expenses, and get the weather information for a specified location. This README provides an overview of the API and its features.

## Table of Contents

- [Installation](#installation)
- [Database Setup](#database-setup)
- [Models](#models)
- [Routes](#routes)
  - [Destination Management](#destination-management)
  - [Itinerary Planning](#itinerary-planning)
  - [Expense Tracking](#expense-tracking)
  - [Weather Route](#weather-route)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/SanketPotdar121695/wanderlust-travel-planner
   ```

2. Change to the project directory:

   ```bash
   cd myapp
   ```

3. Create a virtual environment (recommended) and activate it:

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

The application uses a SQLite database to store destination, itinerary, and expense data. To set up the database, follow the steps below:

1. Create a new SQLite database.

2. Set the database URL as an environment variable. You can add it to a `.env` file:

   ```
   DATABASE_URL=sqlite:///storage.db
   ```

## Models

The application defines the following data models:

- Destination

  - Fields: id, name, description, location, itineraries

- Itinerary

  - Fields: id, destination_id, activity, date

- Expense
  - Fields: id, destination_id, description, amount, date

## Routes

### Destination Management

- **Create a Destination**: `POST /destination`
- **Get All Destinations**: `GET /destinations`
- **Get a Destination by ID**: `GET /destination/<int:destination_id>`
- **Update a Destination by ID**: `PUT /destination/<int:destination_id>`
- **Delete a Destination by ID**: `DELETE /destination/<int:destination_id>`

### Itinerary Planning

- **Create an Itinerary**: `POST /itinerary`
- **Get All Itineraries**: `GET /itineraries`
- **Update an Itinerary by ID**: `PUT /itinerary/<int:itinerary_id>`
- **Delete an Itinerary by ID**: `DELETE /itinerary/<int:itinerary_id>`

### Expense Tracking

- **Create an Expense**: `POST /expense`
- **Get All Expenses**: `GET /expenses`
- **Update an Expense by ID**: `PUT /expense/<int:expense_id>`
- **Delete an Expense by ID**: `DELETE /expense/<int:expense_id>`

### Weather Route

- **Get Weather Data**: `GET /weather?location=CityName`

  Returns weather information for the specified location.

## Usage

1. Start the Flask application:

   ```bash
   python run.py
   ```

2. Access the API using a CLI tool like `git bash` or a web browser.

3. Use the provided routes to manage destinations, itineraries, expenses, and check weather conditions.

## Contributing

Contributions are welcome! Please submit issues or pull requests for any improvements or bug fixes.
