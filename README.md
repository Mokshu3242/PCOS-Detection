## PCOS Detection App

### Overview
The PCOS Detection App is an innovative mobile application designed to help women assess their risk of Polycystic Ovary Syndrome (PCOS). Using a questionnaire and data analysis, the app predicts the risk level based on symptoms and medical history. This tool aims to increase PCOS awareness, support early diagnosis, and empower women with proactive health insights.

### Features
* **Risk Assessment**: Predicts PCOS risk based on user-provided symptoms and medical history.
* **User-Friendly Interface**: Simple questionnaire format for seamless data input.
* **Educational Resources**: Provides information on PCOS, treatments, and support resources.
* **Historical Records**: Stores past assessment results for easy tracking.
* **Privacy and Security**: Ensures confidential handling of user data.

### File Structure
* `app_frontend/`: Contains the Flutter code for the app's user interface.
* `backend/`: Python-based backend for handling requests and processing data.
* `database/`: MongoDB setup and scripts for storing user data and assessment results.
* `models/`: Includes machine learning models for PCOS risk prediction.
* `README.md`: Project overview and instructions.

### Installation

#### Prerequisites
* **Mobile Platform**: Android (primary); may extend to iOS and other platforms.
* **Programming Languages**:
  * **Frontend**: Flutter (Dart)
  * **Backend**: Python (Flask)
  * **Database**: MongoDB for data storage and retrieval.

#### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/pcos-detection-app.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd pcos-detection-app
   ```

3. **Set Up the Backend**:
   * Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   * Start the Flask backend server:
     ```bash
     python backend/app.py
     ```

4. **Configure the Database**:
   * Set up MongoDB and configure database settings in `backend/config.py`.

5. **Run the Frontend**:
   * Open the `app_frontend/` folder in a Flutter-compatible IDE (e.g., Android Studio or VSCode).
   * Connect an Android emulator or device.
   * Run the Flutter app:
     ```bash
     flutter run
     ```

### Usage
1. **Launch the App**:
   * Open the PCOS Detection App on an Android device or emulator.

2. **Complete the Questionnaire**:
   * Answer questions related to menstrual cycles, symptoms, and medical history.
   * Submit responses to receive an immediate PCOS risk assessment.

3. **View Results**:
   * The app will display a risk level (e.g., Low, Medium, High) and provide further guidance.

4. **Access Resources**:
   * Explore educational content on PCOS, including symptoms, treatments, and support networks.
   * Optionally, connect with doctors or support groups via the provided links.

### Model Training
The backend uses a machine learning model trained on symptom and medical history data to predict PCOS risk. For re-training:
1. **Data Collection**: Gather and preprocess user data for training.
2. **Training**: Train models with Python (scikit-learn or TensorFlow).
3. **Evaluation**: Evaluate using metrics like accuracy, precision, and recall to ensure reliability.
4. **Deployment**: Update the model in `models/` for app integration.

### Contributing
1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-name`).
3. **Commit your changes** (`git commit -m 'Add feature'`).
4. **Push to the branch** (`git push origin feature-name`).
5. **Open a Pull Request**.
